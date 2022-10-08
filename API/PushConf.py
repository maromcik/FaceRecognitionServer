import paramiko
import FaceRecognition.models as database


def make_config_file(unipi):
    cameras = database.Camera.objects.filter(unipi=unipi)
    conf = unipi.server_ip + '\n'
    for camera in cameras:
        conf += "{:07d}".format(camera.id) + ';' + camera.stream + '\n'
    return conf


def push():
    print("pushing conf")
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(    paramiko.AutoAddPolicy())
    unipis = database.Unipi.objects.all()
    for unipi in unipis:
        conf = make_config_file(unipi)
        try:
            print("pushing to: ", unipi.ip)
            ssh.connect(unipi.ip, username=unipi.username, password=unipi.password, timeout=5)
            _, _, _ = ssh.exec_command(f"echo \"{conf}\" > configuration.conf")
            print("pushed successfully")
        except TimeoutError:
            print("failed: ", unipi.ip)
            ssh.close()
            return unipi.ip
    ssh.close()
    return 0


def restart_unipis():
    print("restarting all unipis")
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    unipis = database.Unipi.objects.all()
    for unipi in unipis:
        try:
            print("restarting: ", unipi.ip)
            ssh.connect(unipi.ip, username=unipi.username, password=unipi.password, timeout=5)
            _, _, _ = ssh.exec_command(f"docker restart face_rec_rp")
            print("pushed successfully")
        except TimeoutError:
            print("restarting failed: ", unipi.ip)
            ssh.close()
            return unipi.ip
    ssh.close()
    return 0

