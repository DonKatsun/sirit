from django.shortcuts import redirect
from django.urls import reverse


class RedirectOn404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404 or response.status_code==403:
            return redirect(reverse('login_view'))
        return response
