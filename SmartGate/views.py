from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.conf import settings
from django.contrib.auth.decorators import login_required
from FaceRecognition import views



@login_required(login_url='/accounts/login')
@require_GET
# renders home page
def home(request):
    # keys for push notifications
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    user = request.user
    try:
        running = views.rec_threads.facerecognition_thread.isAlive()
    except AttributeError:
        running = False
    return render(request, 'home.html',
                  {user: user, 'vapid_key': vapid_key, 'running': running, 'subscription': "test"})
