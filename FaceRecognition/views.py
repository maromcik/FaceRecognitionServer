import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# renders FaceRecognition template
@login_required(login_url='/accounts/login')
def index(request):
    user = request.user
    return HttpResponse(render(request, 'FaceRecognition/LiveView.html', {'running': True, 'subscription': "test"}))

