from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import render


class LoginView(AuthLoginView):
    template_name = 'registration/login.html'
