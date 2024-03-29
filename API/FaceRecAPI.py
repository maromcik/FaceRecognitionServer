"""
Functions in this file handle face recognition, processing of the staff descriptors,
receiving frames from clients and the logic of logging people.
"""

import os
import pickle
import socket
import numpy as np
import multiprocessing as mp
import threading as mt

from apscheduler.schedulers.background import BackgroundScheduler

import dlib
import cv2
# from arcface import ArcFace

from django.utils import timezone
import FaceRecognition.models as database
from django import db

resnet = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")
# arcface_model = ArcFace.ArcFace()
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

model = "dlib"
N_CPU = mp.cpu_count()


def dlib_dsc(face):
    return np.array(resnet.compute_face_descriptor(face))


# def arcface_dsc(face):
#     return arcface_model.calc_emb(face)


models = {"dlib": dlib_dsc,
          # "arcface": arcface_dsc
          }


def get_descriptor(face, m):
    return models[m](face)


def dlib_compare(descriptors, dsc, threshold):
    # do for every comparison in the list comparisons
    if len(descriptors) == 0:
        return False, -1
    comparisons = np.linalg.norm(descriptors - dsc, axis=1)
    for i in range(len(comparisons)):
        if comparisons[i] <= threshold:
            return True, i
    return False, -1


# def arcface_compare(descriptors, dsc, threshold):
# do for every comparison in the list comparisons
# for i in range(len(descriptors)):
#     dst = arcface_model.get_distance_embeddings(descriptors[i], dsc)
#     print(dst)
#     if dst <= threshold:
#         return True, i
# return False, -1


comparison = {"dlib": dlib_compare,
              # "arcface": arcface_compare
              }


def compare_all(descriptors, dsc, threshold, m):
    return comparison[m](descriptors, dsc, threshold)


"""Calculates descriptor of the face and compares 
it agains the descriptors of people in the building and against staff."""


def process_image(descriptors, staff_descriptors, staff, img):
    if len(detector(img, 1)) != 1:
        print("no face")
        return None, None, None
    dsc = get_descriptor(img, model)
    if staff:
        exists, idx = compare_all(staff_descriptors, dsc, 0.6, model)
        if exists:
            # this person is staff
            print("person is staff")
            return False, idx, False
    if len(descriptors) == 0:
        descriptors.append(dsc)
        # this is a new person and shared descriptors are empty
        return True, 0, True
    exists, idx = compare_all(descriptors, dsc, 0.55, model)
    if exists:
        # this is an existing person
        return True, idx, False
    descriptors.append(dsc)
    # this is a new person
    return True, len(descriptors) - 1, True


"""Depending on the return value of the preceding function it appropriately logs people"""


def process(frame_queue, shared_descriptors, shared_staff_descriptors, person_map, staff):
    # each process should close the connection to the database and recreate a new one.
    db.connections.close_all()
    while True:
        camera_id, frame, time_stamp = frame_queue.get(True)
        # print("q:", frame_queue.qsize())
        # start = time.time()
        camera = database.Camera.objects.get(pk=camera_id)
        room = camera.room
        is_entrance = camera.entrance
        is_exit = camera.exit

        write_db, idx, new_idx = process_image(shared_descriptors, shared_staff_descriptors, staff, frame)

        if not write_db or write_db is None:
            # print("total time: ", time.time() - start)
            continue

        last_person = None
        last_camera = None

        # checks if the person has already been logged.
        if database.Log.objects.all().count() > 0 and idx in person_map:
            last_log = database.Log.objects.filter(person__id=person_map[idx]).latest('time')
            last_person = int(last_log.person.id)
            last_camera = int(last_log.camera.id)

        # and is_entrance and not is_exit
        # and not is_entrance and not is_exit

        # if a person has already been logged with the same camera as before, it should be logged again
        # this protects against continual writing to the database.
        if write_db and last_person is not None and last_camera is not None \
                and camera_id == last_camera and person_map.get(idx, -1) == last_person:
            print(f"skipping {idx}")
        # if an entrance camera detects a new face, it should create the person and log them.
        elif write_db and new_idx and is_entrance and not is_exit:
            print(f"new person with id {idx}")
            person = database.Person.objects.create()
            person_map[idx] = person.id
            database.Log.objects.create(person=person, camera=camera, time=time_stamp)
        # if a camera is neither entrance, nor exit and the person has already been seen. It should only log the person
        elif write_db and not new_idx and not is_entrance and not is_exit:
            if idx in person_map:
                print(f"logging with id {idx}")
                person = database.Person.objects.get(id=person_map[idx])
                database.Log.objects.create(person=person, camera=camera, time=time_stamp)
            else:
                print(f"person {idx} has not entered")
        # if an exit camera detects an existing person, it deletes the person from the database and increments
        # the counter for the room that the camera is located in.
        elif write_db and not new_idx and not is_entrance and is_exit:
            if idx in person_map:
                database.Person.objects.get(id=person_map[idx]).delete()
                del person_map[idx]
                del shared_descriptors[idx]
                room.visited += 1
                room.save()
                print("person has left the buildings")
            # protection because of the concurrent access
            else:
                if 0 <= idx < len(shared_descriptors) and idx not in person_map:
                    del shared_descriptors[idx]
                    print("person has never entered the building")
        # in all the other cases, the person is deleted from the shared descriptors and no further action is performed
        else:
            if 0 <= idx < len(shared_descriptors) and idx not in person_map:
                del shared_descriptors[idx]
                # print("DELETE")
        # print("total time: ", time.time() - start)


def load_staff_descriptors():
    with open('staff_descriptors.pkl', 'rb') as infile:
        staff_descriptors = pickle.load(infile)
    print("Staff descriptors have been loaded")
    return staff_descriptors


"""Periodically prunes logs in an attempt to mitigate the issue of creating multiple people in the database 
from a single physical person. Multiple records in the Person table for a single physical person happen 
because of the concurrent access. Works pretty well."""


def prune_logs(descriptors, person_map):
    print("descriptors", len(descriptors))
    print("personmap", len(person_map), "ids:", person_map)
    i = 0
    while i < len(descriptors):
        comparisons = np.linalg.norm(descriptors - descriptors[i], axis=1)
        # print(comparisons)
        for idx in range(len(comparisons) - 1, -1, -1):
            if 0.01 <= comparisons[idx] <= 0.62:
                if idx in person_map:
                    database.Person.objects.get(id=person_map[idx]).delete()
                    del person_map[idx]
                    del descriptors[idx]
                    print(f"person with {idx} deleted")
                else:
                    if 0 <= idx < len(descriptors):
                        # print(f"no such person, deleting {idx}")
                        del descriptors[idx]
        i += 1


"""Receives an aligned face from a client via sockets"""


def handle_connection(c, frame_queue):
    camera_id = int(c.recv(7).decode())
    fragments = []
    while True:
        chunk = c.recv(4096)
        if not chunk:
            break
        fragments.append(chunk)
    c.close()
    img = np.asarray(bytearray(b''.join(fragments)), dtype="uint8")
    frame = cv2.imdecode(img, cv2.IMREAD_COLOR)
    frame_queue.put((camera_id, frame, timezone.now()))


def infer_ip():
    temp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    temp_s.connect(("8.8.8.8", 80))
    ip = temp_s.getsockname()[0]
    return ip


"""Listens for connections from clients.
Also creates a pool of process that uses a blocking queue to distribute the workload"""


def server_listener():
    manager = mp.Manager()
    shared_descriptors = manager.list()
    shared_staff_descriptors = manager.list()
    person_map = manager.dict()
    staff = False
    try:
        shared_staff_descriptors[:] = load_staff_descriptors()[:]
        staff = True
    except FileNotFoundError:
        print("Creating staff descriptors")
        ret = process_staff_descriptors()
        if ret == 0:
            shared_staff_descriptors[:] = load_staff_descriptors()[:]
            if len(shared_staff_descriptors) > 0:
                staff = True
        else:
            print("Staff file will not be used:")

    pruner = BackgroundScheduler()
    pruner.add_job(prune_logs, 'interval', seconds=30, args=(shared_descriptors, person_map))
    pruner.start()
    frame_queue = mp.Queue()
    pool = mp.Pool(N_CPU - 2, process,
                   (frame_queue, shared_descriptors, shared_staff_descriptors, person_map, staff,), )

    port = int(os.environ.get("SERVER_PORT", default=5555))
    addr = infer_ip(), port
    print("IP: ", addr)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1000)
    while True:
        c, addr = s.accept()
        t = mt.Thread(target=handle_connection, args=(c, frame_queue,), daemon=True)
        t.start()


def run_server():
    p = mp.Process(target=server_listener)
    p.start()
    return p


def load_image(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def process_staff_descriptors_worker(name, image):
    dir_path = os.path.join(os.path.dirname(__file__), "..") + "/media/"
    full_path = dir_path + image
    print("processing: ", full_path)
    img = load_image(full_path)
    face = detector(img, 1)
    descriptor = None
    if len(face) != 0:
        landmarks = sp(img, face[0])
        aligned_face = dlib.get_face_chip(img, landmarks, 150)
        descriptor = get_descriptor(aligned_face, model)
    else:
        print("No face in picture {}".format(full_path))
        database.Staff.objects.filter(name=name).delete()
        print("record deleted from database")
    return descriptor


""""Calculates descriptors of the staff's faces and saves the descriptors to a file via Pickle"""


def process_staff_descriptors():
    db.connections.close_all()
    staff = database.Staff.objects.all()
    names = list(staff.values_list('name', flat=True))
    files = list(staff.values_list('file', flat=True))
    pool = mp.Pool(processes=N_CPU - 1)
    descriptors = (pool.starmap(process_staff_descriptors_worker, zip(names, files)))
    descriptors = [item for item in descriptors if item is not None]
    with open('staff_descriptors.pkl', 'wb') as outfile:
        pickle.dump(descriptors, outfile, pickle.HIGHEST_PROTOCOL)
    outfile.close()
    pool.close()
    pool.terminate()
    print("descriptors of staff have been saved")
    if len(descriptors) == 0:
        print("No staff found")
        return -1
    return 0


def reset_counters():
    for room in database.Room.objects.all():
        room.visited = 0
        room.save()
