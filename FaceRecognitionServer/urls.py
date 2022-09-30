from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView



urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:login'))),
    path('admin/', admin.site.urls),
    path('FaceRecognition/', include('FaceRecognition.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
