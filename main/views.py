from django.shortcuts import render

# Функція для головної сторінки
def index(request):
    return render(request, 'main/index.html')

def curriculum(request):
    return render(request, 'main/curriculum.html')

def instructors(request):
    return render(request, 'main/instructors.html')

def resources(request):
    return render(request, 'main/resources.html')

def registration(request):
    return render(request, 'main/registration.html')

def forum(request):
    return render(request, 'main/forum.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
