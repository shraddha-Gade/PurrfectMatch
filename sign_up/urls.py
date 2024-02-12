from django.urls import path

from . import views

urlpatterns = [
    
    path('sign_up' , views.sign_up , name = 'sign_up'),
    path('signup_submit' , views.signup_submit , name = 'signup_submit')
]