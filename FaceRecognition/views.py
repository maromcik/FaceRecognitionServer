import time

from psutil import Process
import os

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from API import FaceRecAPI
from FaceRecognition.models import Person

# is running
RUNNING = False


@login_required(login_url='/accounts/login')
def start_server(request):
    if start() == 0:
        message = "Face recognition has been started"
        messages.success(request, message)
    else:
        message = "Face recognition is already running."
        messages.warning(request, message)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def stop_server(request):
    if stop() == 0:
        message = "Face recognition has been stopped"
        messages.success(request, message)
    else:
        message = "Face recognition is not running."
        messages.warning(request, message)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def restart_server(request):
    stop()
    time.sleep(1)
    start()
    message = "Face recognition has been restarted"
    messages.success(request, message)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def start():
    global RUNNING
    if not RUNNING:
        p = FaceRecAPI.run_server()
        print("start", p.pid)
        RUNNING = True
        return 0
    return 1


"""Kills all the spawned processes"""


def stop():
    global RUNNING
    if RUNNING:
        parent = Process(os.getpid())
        for child in parent.children(recursive=True):
            print("child: ", child.pid)
            child.kill()
        RUNNING = False
        print("All children killed")
        Person.objects.all().delete()
        print("All persons deleted")
        return 0
    return 1
