from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import User

# Create your views here.
def sign_up(request):
    return render(request, 'sign_up.html')


def signup_submit(request):
    if request.method == 'POST':
        print("signup_submit view reached")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        city = request.POST.get('city')

        user1 = User(first_name = first_name , last_name = last_name , user_name = user_name , contact_no = contact_no , email = email , password = password ,gender = gender ,
                   city = city)
        user1.save()
        n = 'User signed up'
        messages.success(request, 'Signed up Successfully')
        return redirect('home')  # Redirect to the add_pet page after successful form submission

    return render(request, 'sign_up.html')  # Render the same page if the request method is not POST or form submission fails
