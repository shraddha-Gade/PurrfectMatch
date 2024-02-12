# Home_page/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('cat_breeds', views.cat_breeds, name='cat_breeds'),
    path('dog_breeds', views.dog_breeds, name='dog_breeds'),
]
