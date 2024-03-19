# Home_page/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('cat_breeds', views.cat_breeds, name='cat_breeds'),
    path('dog_breeds', views.dog_breeds, name='dog_breeds'),
    #path('add_cat', views.add_cat, name='add_cat'),
    #path('add_dog', views.add_dog, name='add_dog'),
    #path('sign_up', views.sign_up, name='sign_up'),
    #path('logout' , views.logout , name = 'logout'),
    #path('login' , views.login , name = 'login'),
    #path('profile' , views.Myprofile , name = 'profile'),
]
