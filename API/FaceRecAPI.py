import os
import pickle
import socket
import multiprocessing as mp
from apscheduler.schedulers.background import BackgroundScheduler
import dlib
import numpy as np
from django.utils import timezone
from arcface import ArcFace

import FaceRecognition.models as database
import cv2
from django import db


resnet = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")
arcface_model = ArcFace.ArcFace()
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

model = "arcface"


def dlib_dsc(face):
    return np.array(resnet.compute_face_descriptor(face))

def arcface_dsc(face):
    return arcface_model.calc_emb(face)


models = {"dlib": dlib_dsc,
          "arcface": arcface_dsc}


def get_descriptor(face, model):
    return models[model](face)



def dlib_compare(descriptors, dsc, threshold):
    # do for every comparison in the list comparisons
    comparisons = np.linalg.norm(descriptors - dsc, axis=1)
    for i in range(len(comparisons)):
        if comparisons[i] <= threshold:
            return True, i
    return False, -1


def arcface_compare(descriptors, dsc, threshold):
    # do for every comparison in the list comparisons
    for i in range(len(descriptors)):
        dst = arcface_model.get_distance_embeddings(descriptors[i], dsc)
        if dst <= threshold:
            return True, i
    return False, -1

comparison = {"dlib": dlib_compare,
          "arcface": arcface_compare}


def compare_all(descriptors, dsc, threshold, model):
    return comparison[model](descriptors, dsc, threshold)


def process_image(descriptors, staff_descriptors, staff, img):

    if len(detector(img, 1)) != 1:
        print("Invalid face in picture")
        return None, None
    dsc = get_descriptor(img, model)
    if staff:
        exists, idx = compare_all(staff_descriptors, dsc, 0.58, model)
        if exists:
            # this person is staff
            print("person is staff")
            return False, idx
    if len(descriptors) == 0:
        descriptors.append(dsc)
        # this is a new person and shared descriptors are empty
        return True, -1
    exists, idx = compare_all(descriptors, dsc, 0.55, model)
    if exists:
        # this is an existing person
        return True, idx
    descriptors.append(dsc)
    # this is a new person
    return True, -1


def process_connection(c, shared_descriptors, shared_staff_descriptors, staff):
    db.connections.close_all()
    camera_id = int(c.recv(7).decode())
    print(f"camera id: {camera_id}")
    camera = database.Camera.objects.get(pk=camera_id)
    room = camera.room

    fragments = []
    while True:
        chunk = c.recv(4096)
        if not chunk:
            break
        fragments.append(chunk)

    c.close()
    img = np.asarray(bytearray(b''.join(fragments)), dtype="uint8")
    frame = cv2.imdecode(img, cv2.IMREAD_COLOR)
    write_db, idx = process_image(shared_descriptors, shared_staff_descriptors, staff, frame)

    last_person = None
    last_camera = None
    if database.Log.objects.all().count() > 0:
        last_log = database.Log.objects.latest('time')
        last_person = int(last_log.person.id_in_dsc)
        last_camera = int(last_log.camera.id)

    if write_db and last_person is not None and last_camera is not None and camera_id == last_camera and int(idx) == last_person:
        print("skipping logging")
    elif write_db and idx == -1:
        print(f"creating new person with id {len(shared_descriptors) - 1}")
        person = database.Person.objects.create(id_in_dsc=len(shared_descriptors) - 1)
        database.Log.objects.create(person=person, camera=camera, room=room, time=timezone.now())
    elif write_db and idx != -1:
        print(f"logging person with id {idx}")
        person = database.Person.objects.get(id_in_dsc=idx)
        database.Log.objects.create(person=person, camera=camera, room=room, time=timezone.now())
    exit(0)


def load_staff_descriptors():
    with open('staff_descriptors.pkl', 'rb') as infile:
        staff_descriptors = pickle.load(infile)
    print("Staff descriptors have been loaded")
    return staff_descriptors


def prune_logs(descriptors):
    print("Pruning")
    i = 0
    while i < len(descriptors):
        comparisons = np.linalg.norm(descriptors - descriptors[i], axis=1)
        for j in range(len(comparisons)):
            if 0.01 <= comparisons[j] <= 0.6:
                print(j, comparisons[j])
                descriptors.pop(j)
        i += 1
        print("length:", len(descriptors))

    # for i in range(len(descriptors)):
    #     comparisons = np.linalg.norm(descriptors - descriptors[i], axis=1)
    #     for j in range(len(comparisons)):
    #         if 0.01 <= comparisons[j] <= 0.6:


def server_listener(s):
    manager = mp.Manager()
    shared_descriptors = manager.list()
    shared_staff_descriptors = manager.list()
    staff = True
    try:
        shared_staff_descriptors[:] = load_staff_descriptors()[:]
    except FileNotFoundError:
        print("Creating staff descriptors")
        ret = process_staff_descriptors()
        if ret == 0:
            shared_staff_descriptors[:] = load_staff_descriptors()[:]
        else:
            staff = False
            print("Staff file will not be used:")

    pruner = BackgroundScheduler()
    pruner.add_job(prune_logs, 'interval', seconds=30, args=(shared_descriptors,))
    pruner.start()

    s.listen(1000)
    while True:
        c, addr = s.accept()
        # print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        p = mp.Process(target=process_connection, args=(c, shared_descriptors, shared_staff_descriptors, staff), daemon=True)
        p.start()



def load_image(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def process_staff_descriptors_worker(name, file):
    dir_path = os.path.join(os.path.dirname(__file__), "..") + "/media/"
    full_path = dir_path + file
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


def process_staff_descriptors():
    db.connections.close_all()
    staff = database.Staff.objects.all()
    names = list(staff.values_list('name', flat=True))
    files = list(staff.values_list('file', flat=True))
    pool = mp.Pool(processes=mp.cpu_count())
    descriptors = (pool.starmap(process_staff_descriptors_worker, zip(names, files)))
    descriptors = [item for item in descriptors if item is not None]
    with open('staff_descriptors.pkl', 'wb') as outfile:
        pickle.dump(descriptors, outfile, pickle.HIGHEST_PROTOCOL)
    outfile.close()
    print("descriptors of staff have been saved")

    if len(descriptors) == 0:
        print("No staff found")
        return -1
    return 0

class FaceRecognition:
    def __init__(self):

        temp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_s.connect(("8.8.8.8", 80))
        self.port = 5555
        self.ip = temp_s.getsockname()[0]
        self.addr = self.ip, self.port
        print("IP: ", self.addr)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # def __del__(self):
    #     for child in active_children():
    #         child.terminate()
    #     print("All children killed")
    #     self.s.close()
    #     print("Server closed")

    def run_server(self):
        self.s.bind(self.addr)

        p = mp.Process(target=server_listener, args=(self.s, ))
        p.start()



