import paramiko
import FaceRecognition.models as database


def make_config_file(client):
    # cameras = database.Camera.objects.filter(client=client)
    # conf = client.server_ip + '\n'
    # for camera in cameras:
    #     conf += "{:07d}".format(camera.id) + ';' + camera.stream + '\n'
    # return conf
    conf = client.server_ip + '\n'
    conf += "{:07d}".format(client.camera1.id) + ';' + client.camera1.stream + '\n'
    if client.camera2 is not None:
        conf += "{:07d}".format(client.camera2.id) + ';' + client.camera2.stream + '\n'
    return conf


def push():
    print("pushing conf")
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    clients = database.Client.objects.all()
    for client in clients:
        if client.ssh:
            conf = make_config_file(client)
            try:
                print("pushing to: ", client.ip)
                ssh.connect(client.ip, username=client.username, password=client.password, timeout=5)
                _, _, _ = ssh.exec_command(f"echo \"{conf}\" > configuration.conf")
                print("pushed successfully")
            except (paramiko.AuthenticationException, TimeoutError):
                print("failed: ", client.ip)
                ssh.close()
                return client.ip
        else:
            print("NOT pushing to: ", client.ip)
    ssh.close()
    return 0


def restart_docker():
    print("restarting all clients")
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    clients = database.Client.objects.all()
    for client in clients:
        if client.ssh:
            try:
                print("restarting: ", client.ip)
                ssh.connect(client.ip, username=client.username, password=client.password, timeout=5)
                _, _, _ = ssh.exec_command("docker restart fr")
                print("restarted successfully")
            except (paramiko.AuthenticationException, TimeoutError):
                print("restarting failed: ", client.ip)
                ssh.close()
                return client.ip
        else:
            print("NOT restarting: ", client.ip)
    ssh.close()
    return 0

