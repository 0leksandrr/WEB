from django.shortcuts import render
from .models import Product


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

    if my_id == 1:
        template_name = 'courses/python.html'
    elif my_id == 2:
        template_name = 'courses/javascript.html'
    elif my_id == 3:
        template_name = 'courses/android_ios.html'
    elif my_id == 4:
        template_name = 'courses/devops.html'

    return render(request, template_name, context=context)
