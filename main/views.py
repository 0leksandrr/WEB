from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def curriculum(request):
    return render(request, 'main/curriculum.html')

def instructors(request):
    return render(request, 'main/instructors.html')

def resources(request):
    return render(request, 'main/resources.html')

def forum(request):
    return render(request, 'main/forum.html')

def about(request):
    return render(request, 'main/about.html')
