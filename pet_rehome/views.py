from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cat , Dog

def add_cat(request):
    return render(request, 'add_cat.html')

def add_dog(request):
    return render(request, 'add_dog.html')

def submitted_cat(request):
    if request.method == 'POST':
        print("Submitted view reached")
        name = request.POST.get('pet_name')
        gender = request.POST.get('pet_gender')
        breed = request.POST.get('pet_breed')
        age = request.POST.get('pet_age')
        vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        city = request.POST.get('pet_city')
        description = request.POST.get('pet_description')
        image = request.FILES.get('pet_image')

        pet1 = Cat(name=name, gender=gender, breed=breed, age=age, vaccinated=vaccinated,
                   city=city, description=description, image=image)
        pet1.save()
        n = 'Pet Added'
        messages.success(request, 'Pet Added Successfully')
        return redirect('home')  # Redirect to the add_pet page after successful form submission

    return render(request, 'add_cat.html')  # Render the same page if the request method is not POST or form submission fails

def submitted_dog(request):
    if request.method == 'POST':
        print("Submitted view reached")
        name = request.POST.get('pet_name')
        gender = request.POST.get('pet_gender')
        breed = request.POST.get('pet_breed')
        age = request.POST.get('pet_age')
        vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        city = request.POST.get('pet_city')
        description = request.POST.get('pet_description')
        image = request.FILES.get('pet_image')

        pet1 = Dog(name=name, gender=gender, breed=breed, age=age, vaccinated=vaccinated,
                   city=city, description=description, image=image)
        pet1.save()
        n = 'Pet Added'
        messages.success(request, 'Pet Added Successfully')
        return redirect('home')  # Redirect to the add_pet page after successful form submission

    return render(request, 'add_dog.html')  # Render the same page if the request method is not POST or form submission fails
