from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import View
from user.forms import UserRegistrationForm


class LoginView(AuthLoginView):
    template_name = 'registration/login.html'


class RegistrationView(TemplateResponseMixin, View):
    template_name = 'registration/registration.html'

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            User.objects.create_user(
                username=cleaned_data['username'],
                email=cleaned_data['email'],
                password=cleaned_data['password']
            ).save()
            return redirect(reverse('user:login'))

        return self.render_to_response({'form': form})

