from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('instructors/', views.instructors, name='instructors'),
    path('resources/', views.resources, name='resources'),
    path('forum/', views.forum, name='forum'),
    path('about/', views.about, name='about'),
]
