from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'landing.html')


def about(request):
    return render(request, 'about.html')

def gallery(request):
    
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()

    context = {}
    context['categories'] = categories
    context['images']= images
    context['locations']= locations

   

    return render(request, 'gallery.html', context )



def categoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'category.html', context)


def imageDetailPage(request, slug1, slug2):


    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)
    

    context = {}
    context['category'] = category
    context['image'] = image


    return render(request, 'image.html', context)

def photo(request, slug,title):
    location = Location.objects.get(title=title)

    image = Image.objects.get(slug=slug)

    context = {}
    
    context['image'] = image
    context['location'] = location
    return render(request, 'photo.html', context)

def locationPage(request, slug):

    location = Location.objects.get(slug=slug)
    images = Image.objects.filter(location=location).order_by('-date_created')[:6]
    
    context = {}
    context['location'] = location
    context['images'] = images
    

    return render(request, 'location.html', context)

def locationDetailPage(request, slug1, slug2):


    location= Location.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)
    

    context = {}
    context['location'] = location
    context['image'] = image


    return render(request, 'locationd.html', context)

