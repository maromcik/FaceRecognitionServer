from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from . import views


app_name = 'FaceRecognition'
urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:login'))),
    path('start', views.start_server, name='start'),
    path('stop', views.stop_server, name='stop'),
    path('restart', views.restart_server, name='restart'),
]
