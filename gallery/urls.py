from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('about/', views.about, name='gallery-about'),
    path('gallery/',views.gallery,name = 'gallery'),
    path('category/<slug:slug>', views.categoryPage, name='image-category'),
    path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
    
    path('images/<slug:slug>', views.photo, name='photo'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)