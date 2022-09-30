from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from FaceRecognition.models import Person, Log, Camera, Staff
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import path
from FaceRecognition import views
from django.http import HttpResponseRedirect
from django.contrib import messages
from API import FaceRecAPI



class PersonAdmin(admin.ModelAdmin):
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

# redefines admin interface behaviour
class LogAdmin(admin.ModelAdmin):
    # field options
    list_display = ['person', 'time']
    # list_filter = ['time', 'granted']
    # search_fields = ['person__name']
    # readonly_fields = ['person', 'time', 'granted', 'snapshot']

    # you cannot change logs
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

    # there's an image (snapshot)
    def image_tag(self, obj):
        try:
            return mark_safe('<img src="{url}" height={height} />'.format(
                url=obj.snapshot.url,
                height=150,
            )
            )
        except ValueError:
            pass

    image_tag.short_description = 'Image'


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
            height=150,
        )
        )

    image_tag.short_description = 'Image'


class CameraAdmin(admin.ModelAdmin):
    pass


# registers all the models
admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Camera, CameraAdmin)

admin.site.site_header = "Face Recognition Administration"
