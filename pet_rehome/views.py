from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pet

def add_pet(request):
    return render(request, 'add_pet.html')

def submitted(request):
    if request.method == 'POST':
        print("Submitted view reached")
        name = request.POST.get('pet_name')
        species = request.POST.get('pet_species')
        gender = request.POST.get('pet_gender')
        breed = request.POST.get('pet_breed')
        age = request.POST.get('pet_age')
        vaccinated = True if request.POST.get('pet_vaccinated') == 'yes' else False
        city = request.POST.get('pet_city')
        description = request.POST.get('pet_description')
        image = request.FILES.get('pet_image')

        pet1 = Pet(name=name, species=species, gender=gender, breed=breed, age=age, vaccinated=vaccinated,
                   city=city, description=description, image=image)
        pet1.save()
        n = 'Pet Added'
        messages.success(request, 'Pet Added Successfully')
        return redirect('add_pet')  # Redirect to the add_pet page after successful form submission

    return render(request, 'add_pet.html')  # Render the same page if the request method is not POST or form submission fails
