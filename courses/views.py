from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Створюйте ваші функції тут.
def courses(request):
    items = Product.objects.all()
    item_name = request.GET.get('search', '')
    
    if item_name:
        items = items.filter(name__icontains=item_name)

    context = {'items': items, 'search_term': item_name}
    return render(request, 'courses/courses.html', context)

def coursesItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {'item': item}
    return render(request, 'courses/detail.html', context=context)
