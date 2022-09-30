import os
import pickle
import socket
import multiprocessing as mp
import dlib
import numpy as np
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
    pool = mp.Pool(processes=6)
    descriptors = (pool.starmap(process_staff_descriptors_worker, zip(names, files)))
    descriptors = [item for item in descriptors if item is not None]
    with open('staff_descriptors.pkl', 'wb') as outfile:
        pickle.dump(descriptors, outfile, pickle.HIGHEST_PROTOCOL)
    outfile.close()
    print("descriptors of known people has been saved")

    if len(descriptors) == 0:
        print("No staff found")
        return -1
    return 0


def get_descriptor(face_chip):
    return np.array(resnet.compute_face_descriptor(face_chip))


def compare(known, unknown):
    return np.linalg.norm(known - unknown, axis=1)


def load_staff_descriptors():
    with open('staff_descriptors.pkl', 'rb') as infile:
        staff_descriptors = pickle.load(infile)
    print("Staff descriptors have been loaded")
    return staff_descriptors


def process_image(descriptors, staff_descriptors, staff, img):
    pic = dlib.load_rgb_image(f"/home/user/Pictures/test/{img}.jpg")
    dsc = get_descriptor(pic)
    descriptors.append(dsc)
    print("shared: ", compare(descriptors, get_descriptor(dlib.load_rgb_image(f"/home/user/Pictures/test/5.jpg"))).tolist())
    if staff:
        print("shared staff: ", compare(staff_descriptors, dsc).tolist())


def process_connection(c, shared_descriptors, shared_staff_descriptors, staff):
    c.send(str.encode('You are now connected to the replay server... Type BYE to stop'))

    while True:
        data = c.recv(2048)
        message = data.decode('utf-8')
        if message.strip() == 'BYE':
            break
        process_image(shared_descriptors, shared_staff_descriptors, staff, int(message.strip()))
        reply = f'Server: {message}'
        c.sendall(str.encode(reply))
    c.close()
    print("client closed")
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
        print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        p = mp.Process(target=process_connection, args=(c, shared_descriptors, shared_staff_descriptors, staff), daemon=True)
        p.start()
        print(shared_descriptors)


class FaceRecognition:
    def __init__(self):

        temp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_s.connect(("8.8.8.8", 80))
        self.port = 5432
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







