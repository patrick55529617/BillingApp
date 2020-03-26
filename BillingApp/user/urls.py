from django.urls import path
from user.views import LoginView

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]
