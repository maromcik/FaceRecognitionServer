import paramiko
import FaceRecognition.models as database


def make_config_file(unipi):
    cameras = database.UniPiCamera.objects.filter(unipi=unipi)
    conf = ""
    for camera in cameras:
        conf += str(camera.camera.id) + ';' + camera.camera.stream + '\n'
    return conf


def push():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    unipis = database.UniPi.objects.all()
    for unipi in unipis:
        conf = make_config_file(unipi)
        ssh.connect(unipi.ip, username=unipi.username, password=unipi.password)
        _, _, _ = ssh.exec_command(f"echo \"{conf}\" > configuration.conf")
    print("pushing conf")