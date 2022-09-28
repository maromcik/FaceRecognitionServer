import os
import socket
import multiprocessing as mp
import dlib
import FaceRecognition.models as database

# resnet = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")


# def process(c):
#     img = dlib.load_rgb_image("/home/user/Pictures/test/3.jpg")
#     print(resnet.compute_face_descriptor(img))
#
#

def process_image(c):
    c.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
    # process(c)
    while True:
        data = c.recv(2048)
        message = data.decode('utf-8')
        if message.strip() == 'BYE':
            break
        reply = f'Server: {message}'
        c.sendall(str.encode(reply))
    c.close()
    print("client closed")


    exit(0)


def server_listener(s):
    s.listen(1000)
    while True:
        c, addr = s.accept()
        print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        p = mp.Process(target=process_image, args=(c,))
        p.start()


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
