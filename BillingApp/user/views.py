from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from BillingApp import settings

class LoginView(AuthLoginView):
    template_name = 'registration/login.html'

class LogoutView(AuthLogoutView):
    next_page = settings.LOGIN_URL