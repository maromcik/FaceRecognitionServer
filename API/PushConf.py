import paramiko
import FaceRecognition.models as database


def make_config_file(unipi):
    # cameras = database.Camera.objects.filter(unipi=unipi)
    # conf = unipi.server_ip + '\n'
    # for camera in cameras:
    #     conf += "{:07d}".format(camera.id) + ';' + camera.stream + '\n'
    # return conf
    conf = unipi.server_ip + '\n'
    conf += "{:07d}".format(unipi.camera1.id) + ';' + unipi.camera1.stream + '\n'
    if unipi.camera2 is not None:
        conf += "{:07d}".format(unipi.camera2.id) + ';' + unipi.camera2.stream + '\n'
    return conf


def push():
    print("pushing conf")
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    unipis = database.Unipi.objects.all()
    for unipi in unipis:
        if unipi.push:
            conf = make_config_file(unipi)
            try:
                print("pushing to: ", unipi.ip)
                ssh.connect(unipi.ip, username=unipi.username, password=unipi.password, timeout=5)
                _, _, _ = ssh.exec_command(f"echo \"{conf}\" > configuration.conf")
                print("pushed successfully")
            except (paramiko.AuthenticationException, TimeoutError):
                print("failed: ", unipi.ip)
                ssh.close()
                return unipi.ip
        else:
            print("NOT pushing to: ", unipi.ip)
    ssh.close()
    return 0


def restart_docker():
    print("restarting all unipis")
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    unipis = database.Unipi.objects.all()
    for unipi in unipis:
        if unipi.restart:
            try:
                print("restarting: ", unipi.ip)
                ssh.connect(unipi.ip, username=unipi.username, password=unipi.password, timeout=5)
                _, _, _ = ssh.exec_command("docker restart fr")
                print("restarted successfully")
            except (paramiko.AuthenticationException, TimeoutError):
                print("restarting failed: ", unipi.ip)
                ssh.close()
                return unipi.ip
        else:
            print("NOT restarting: ", unipi.ip)
    ssh.close()
    return 0

