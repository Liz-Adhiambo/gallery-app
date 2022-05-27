from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = Image.get_all_images()
    title = 'lizgalleria'
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories


    return render(request, 'gallery.html', context)

def categoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'category.html', context)