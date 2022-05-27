from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

def home(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = Image.get_all_images()
    title = 'lizgalleria'

    return render(request, 'gallery.html', {'title':title, 'images':images})
