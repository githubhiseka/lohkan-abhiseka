from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User

class DemoAutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEMO_MODE and not request.user.is_authenticated:
            try:
                demo_user = User.objects.get(username="demo")
                login(request, demo_user)
            except User.DoesNotExist:
                pass

        return self.get_response(request)
