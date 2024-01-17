from django.urls import path
from .views import resource  

urlpatterns = [
    path('', resource, name='resource'),  
]
