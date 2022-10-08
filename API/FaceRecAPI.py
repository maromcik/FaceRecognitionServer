import os
import pickle
import socket
import multiprocessing as mp
import dlib
import numpy as np
from django.utils import timezone

import FaceRecognition.models as database
import cv2
from django import db


resnet = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")


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
        descriptor = np.array(resnet.compute_face_descriptor(img, landmarks))
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


def get_descriptor(face_chip):
    return np.array(resnet.compute_face_descriptor(face_chip))


def load_staff_descriptors():
    with open('staff_descriptors.pkl', 'rb') as infile:
        staff_descriptors = pickle.load(infile)
    print("Staff descriptors have been loaded")
    return staff_descriptors


def compare_all(descriptors, dsc):
    # do for every comparison in the list comparisons
    comparisons = np.linalg.norm(descriptors - dsc, axis=1)
    for i in range(len(comparisons)):
        if comparisons[i] <= 0.50:
            return True, i
    return False, -1


def process_image(descriptors, staff_descriptors, staff, img):
    if len(detector(img, 1)) != 1:
        print("Invalid face in picture")
        return None, None
    dsc = get_descriptor(img)
    if staff:
        exists, idx = compare_all(staff_descriptors, dsc)
        if exists:
            print("person is staff")
            return False, idx
    if len(descriptors) == 0:
        descriptors.append(dsc)
        print("new first person")
        return True, -1
    exists, idx = compare_all(descriptors, dsc)
    if exists:
        print("existing person")
        return True, idx
    descriptors.append(dsc)
    print("new person")
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
    print(len(shared_descriptors))
    if write_db and idx == -1:
        print(f"creating new person with id {len(shared_descriptors) - 1}")
        person = database.Person.objects.create(id_in_dsc=len(shared_descriptors) - 1)
        database.Log.objects.create(person=person, camera=camera, room=room, time=timezone.now())
    elif write_db and idx != -1:
        print(f"logging person with id {idx}")
        person = database.Person.objects.get(id_in_dsc=idx)
        database.Log.objects.create(person=person, camera=camera, room=room, time=timezone.now())
    exit(0)


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
    s.listen(1000)
    while True:
        c, addr = s.accept()
        # print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        p = mp.Process(target=process_connection, args=(c, shared_descriptors, shared_staff_descriptors, staff), daemon=True)
        p.start()


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







