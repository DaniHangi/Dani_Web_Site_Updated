# from django.http import Http404
from urllib import request
from twomodels.models import *
from django.shortcuts import get_object_or_404, render   # type: ignore


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    developer = get_object_or_404(Developer, name="Dani")
    
    return render(request, 'pages/service.html', {'developer': developer})


def contact(request):
    return render(request, 'pages/contact.html')


