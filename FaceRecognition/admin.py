from django.contrib import admin
from django.contrib.admin import display
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages

from FaceRecognition.models import *
from API import FaceRecAPI, PushConf


def run_push_conf(request):
    ret = PushConf.push()
    if ret == 0:
        message = "Configuration successfully pushed over SSH"
        messages.success(request, message)
    else:
        message = f"Configuration push failed, check device with IP: {ret}"
        messages.error(request, message)


def run_restart_docker(request):
    ret = PushConf.restart_docker()
    if ret == 0:
        message = "All Docker containers successfully restarted over SSH"
        messages.success(request, message)
    else:
        message = f"Docker restart failed, check device with IP: {ret}"
        messages.error(request, message)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id']
    readonly_fields = ['id']

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
    list_display = ['person', 'time', 'camera', 'get_room']

    # readonly_fields = ['person', 'time', 'camera']

    @display(ordering='camera__room', description='Room')
    def get_room(self, obj):
        return obj.camera.room

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
        self.message_user(request, "Descriptors for staff created")
        return HttpResponseRedirect("../")

    # there's an image of known person in the fields
    def image_tag(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.file.url,
            height=150, ))

    image_tag.short_description = 'Image'


class CameraAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'name', 'stream', 'room', 'entrance', 'exit']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip', 'get_cameras', 'get_server_ip', 'ssh_access']
    change_list_template = "FaceRecognition/change_list2.html"

    def save_related(self, request, form, formsets, change):
        super(ClientAdmin, self).save_related(request, form, formsets, change)
        n_cameras = form.instance.cameras.count()
        if n_cameras > 2:
            message = f"{n_cameras} cameras selected. Make sure \"{form.instance.name}\" is not a Unipi."
            messages.warning(request, message)

    @display(ordering='cameras', description='Cameras')
    def get_cameras(self, obj):
        out = []
        for camera in obj.cameras.all():
            out.append(camera.name)
        return out

    @display(ordering='server__ip', description='Server IP')
    def get_server_ip(self, obj):
        return obj.server.ip

    @display(ordering='ssh_profile__username', description='SSH Profile')
    def get_ssh_profile(self, obj):
        return obj.ssh_profile.username

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
    change_list_template = "FaceRecognition/change_list3.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('reset/', self.reset_counters),
        ]
        return my_urls + urls

    # add functionality to custom buttons
    @method_decorator(login_required(login_url='/admin/login'))
    def reset_counters(self, request):
        FaceRecAPI.reset_counters()
        self.message_user(request, "All counters reset")
        return HttpResponseRedirect("../")


class SSHProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'encrypted_password']


class ServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip']


admin.site.register(Client, ClientAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Camera, CameraAdmin)
admin.site.register(SSHProfile, SSHProfileAdmin)
admin.site.register(Server, ServerAdmin)

admin.site.site_header = "Face Recognition Administration"
