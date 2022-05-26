from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('about/', views.about, name='gallery-about'),
]