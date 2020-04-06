from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    confirmed_password = forms.CharField(
        max_length=30, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmed_password = cleaned_data.get("confirmed_password")

        if password != confirmed_password:
            raise forms.ValidationError(
                "password and confirm_password does not match")
