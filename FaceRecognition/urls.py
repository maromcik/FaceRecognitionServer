from django.urls import path, include

from . import views


app_name = 'FaceRecognition'
urlpatterns = [
    path('', views.index, name='index'),
]
