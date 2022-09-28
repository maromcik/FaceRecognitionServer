from psutil import Process
import os

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from API.FaceRecAPI import FaceRecognition

RUNNING = False


@login_required(login_url='/accounts/login')
def start_server(request):
    global RUNNING
    if not RUNNING:
        fr = FaceRecognition()
        fr.run_server()
        RUNNING = True
        message = "Face recognition has been started"
        messages.success(request, message)
    else:
        message = "Face recognition is already running."
        messages.warning(request, message)
    return redirect("admin:index")


def stop_server(request):
    global RUNNING
    if RUNNING:
        parent = Process(os.getpid())
        for child in parent.children(recursive=True):
            child.kill()
        RUNNING = False
        print("All children killed")
        message = "Face recognition has been stopped"
        messages.success(request, message)
    else:
        message = "Face recognition is not running."
        messages.warning(request, message)
    return redirect("admin:index")