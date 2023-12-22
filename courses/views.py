from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def courses(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, 'courses\courses.html', context)
    
def coursesItem(request, my_id):
    item = Product.objects.get(id = my_id)
    context = {
        'item': item
    }
    return render(request, 'courses\detail.html', context = context)
    
    