from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')

def cat_breeds(request):
    return render(request, 'cat_breeds.html')

def add_cat(request):
    return render(request, 'add_cat.html')

def add_dog(request):
    return render(request, 'add_dog.html')


def dog_breeds(request):
    return render(request, 'dog_breeds.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def login(request):
    return render(request, 'login_form.html')