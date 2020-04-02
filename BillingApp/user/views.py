from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

class LoginView(AuthLoginView):
    template_name = 'registration/login.html'

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login')