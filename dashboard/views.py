from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import AboutMe


def home(request):
    about_me = AboutMe.objects.first()
    context = {
        "about_me": about_me
    }
    return render(request, 'index.html', context=context)
