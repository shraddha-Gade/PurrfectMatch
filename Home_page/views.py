from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')

def cat_breeds(request):
    return render(request, 'cat_breeds.html')

def dog_breeds(request):
    return render(request, 'dog_breeds.html')