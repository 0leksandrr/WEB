from django.shortcuts import render
from .models import Teacher

def index(request):
    return render(request, 'main/index.html')

def curriculum(request):
    return render(request, 'main/curriculum.html')

def instructors(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'main/instructors.html', {'teachers': teachers_list})

def forum(request):
    return render(request, 'main/forum.html')

def about(request):
    return render(request, 'main/about.html')
