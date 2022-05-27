from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('about/', views.about, name='gallery-about'),
    path('gallery/',views.gallery,name = 'gallery'),
    path('category/<slug:slug>', views.categoryPage, name='image-category'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)