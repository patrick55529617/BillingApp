from django.urls import path
from user.views import LoginView, Logout

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout, name='logout')
]
