import paramiko
import FaceRecognition.models as database

"""Crates a configuration string in a predetermined format."""


def make_config_file(client):
    conf = client.server.ip + '\n'
    for camera in client.cameras.all():
        conf += "{:07d}".format(camera.id) + ';' + camera.stream + '\n'
    return conf


"""The following two functions connect to each client in the database that is supposed to be access, 
and echo the configuration or restart the Docker container"""


def execute(ssh, client, command, action):
    try:
        print(f"{action}: ", client.ip)
        ssh.connect(client.ip, username=client.ssh_profile.username, password=client.ssh_profile.password, timeout=5)
        _, _, _ = ssh.exec_command(command)
        print(f"{action} successful")
        return 0
    except (paramiko.AuthenticationException, TimeoutError, paramiko.ssh_exception.NoValidConnectionsError,
            paramiko.ssh_exception.AuthenticationException):
        print(f"{action} failed: ", client.ip)
        ssh.close()
        return client.ip


def connect():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys(filename=None)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    clients = database.Client.objects.all()
    return ssh, clients


def push():
    print("pushing conf")
    ssh, clients = connect()
    for client in clients:
        if client.ssh_access:
            conf = make_config_file(client)
            command = f"echo \"{conf}\" > configuration.conf"
            ret = execute(ssh, client, command, "push")
            if ret != 0:
                return ret
        else:
            print("NOT pushing to: ", client.ip)
    ssh.close()
    return 0


def restart_docker():
    print("restarting selected clients")
    ssh, clients = connect()
    for client in clients:
        if client.ssh_access:
            ret = execute(ssh, client, "docker restart fr", "restart")
            if ret != 0:
                return ret
        else:
            print("NOT restarting: ", client.ip)
    ssh.close()
    return 0
