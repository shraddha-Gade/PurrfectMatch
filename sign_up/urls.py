from django.urls import path

from . import views

urlpatterns = [
    
    path('sign_up' , views.sign_up , name = 'sign_up'),
    path('login_form' , views.login_user , name = 'login'),
    path('login_view' , views.login_view , name = 'login_view'),
    path('signup_submit' , views.signup_submit , name = 'signup_submit')
]