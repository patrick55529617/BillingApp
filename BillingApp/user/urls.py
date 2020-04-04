from django.urls import path
from user import views

app_name = 'user'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/',
         views.RegistrationView.as_view(), name='registration')
]
