from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html

from FaceRecognition.models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import path
from FaceRecognition import views
from django.http import HttpResponseRedirect
from django.contrib import messages
from API import FaceRecAPI, PushConf


def run_push_conf(request):
    ret = PushConf.push()
    if ret == 0:
        message = "Configuration successfully pushed over SSH!"
        messages.success(request, message)
    else:
        message = f"Configuration push failed, check device with IP: {ret}!"
        messages.error(request, message)


def run_restart_docker(request):
    ret = PushConf.restart_docker()
    if ret == 0:
        message = "All Docker containers successfully restarted over SSH!"
        messages.success(request, message)
    else:
        message = f"Docker restart failed, check device with IP: {ret}!"
        messages.error(request, message)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id']

    def has_add_permission(self, request, obj=None):
        if request.user.username == "admin":
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.username == "admin":
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == "admin":
            return True
        return False


class LogAdmin(admin.ModelAdmin):
    list_display = ['person', 'time', 'camera', 'room']

    # def get_camera_location(self, obj):
    #     return obj.camera.location
    #
    # get_camera_location.admin_order_field = 'camera_location'  # Allows column order sorting
    # get_camera_location.short_description = 'Location of the camera'  # Renames column head

    def has_add_permission(self, request, obj=None):
        if request.user.username == "admin":
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.username == "admin":
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == "admin":
            return True
        return False


class StaffAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fields = ['name', 'file']
    list_display = ['name', 'image_tag']
    change_list_template = "FaceRecognition/change_list.html"

    # add links to custom buttons
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('encoding/', self.run_encodings),
        ]
        return my_urls + urls

    # add functionality to custom buttons
    @method_decorator(login_required(login_url='/admin/login'))
    def run_encodings(self, request):
        FaceRecAPI.process_staff_descriptors()
        self.message_user(request, "Encodings done!")
        return HttpResponseRedirect("../")

    # there's an image of known person in the fields
    def image_tag(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.file.url,
            height=150,))

    image_tag.short_description = 'Image'


class CameraAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'stream', 'room']


class UniPiAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip', 'server_ip', 'camera1', 'camera2']
    change_list_template = "FaceRecognition/change_list2.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('push/', self.push_conf),
            path('restart/', self.restart_docker)
        ]
        return my_urls + urls

    # add functionality to custom buttons
    @method_decorator(login_required(login_url='/admin/login'))
    def push_conf(self, request):
        run_push_conf(request)
        return HttpResponseRedirect("../")

    def restart_docker(self, request):
        run_restart_docker(request)
        return HttpResponseRedirect("../")


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'visited']


admin.site.register(Unipi, UniPiAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Camera, CameraAdmin)

admin.site.site_header = "Face Recognition Administration"
