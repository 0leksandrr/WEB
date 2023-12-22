from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name = 'courses'),
    path('<int:my_id>/', views.coursesItem, name = 'coursesItem'),
]

