import paramiko
import FaceRecognition.models as database


def make_config_file(unipi):
    cameras = database.UniPiCamera.objects.filter(unipi=unipi)
    print(cameras.values_list())


def push():
    ssh = paramiko.SSHClient
    unipis = database.UniPi.objects.all()
    print(unipis.values_list())
    for unipi in unipis:
        make_config_file(unipi)

    print("pushing")