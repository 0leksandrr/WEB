from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Відправка електронного листа
            subject = 'Ласкаво просимо на наш сайт!'
            message = 'Дякуємо за реєстрацію. Ви тепер можете насолоджуватися нашими послугами.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [user.email]
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            return redirect('courses')
    form = NewUserForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request, 'users/profile.html')