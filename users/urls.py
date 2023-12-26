from django.urls import path
from .views import register, profile
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/', profile, name='profile'),
]
