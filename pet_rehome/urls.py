from django.urls import path

from . import views

urlpatterns = [
    
    path('add_cat' , views.add_cat , name = 'add_cat'),
    path('add_dog' , views.add_dog , name = 'add_dog'),
    path('submitted_cat' , views.submitted_cat , name = 'submitted_cat'),
    path('submitted_dog' , views.submitted_dog , name = 'submitted_dog')
]