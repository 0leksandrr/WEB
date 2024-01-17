from django.urls import path
from .views import resource, download_pdf

urlpatterns = [
    path('', resource, name='resource'),
    path('download/<int:pk>/', download_pdf, name='download_pdf'),
]
