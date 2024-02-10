from django.urls import path

from . import views

urlpatterns = [
    
    path('add_pet' , views.add_pet , name = 'add_pet'),
    path('submitted' , views.submitted , name = 'submitted')
]