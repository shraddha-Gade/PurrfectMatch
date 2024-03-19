from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
#from .models import User
from django.contrib.auth.views import LogoutView

# Logout view
logout_view = LogoutView.as_view(next_page = 'home')

# Create your views here.
def sign_up(request):
    return render(request, 'sign_up.html')

def login_user(request):
    return render(request, 'login_form.html')

def login_view(request):
    print("login_view view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            # Return an error message or render the login page with an error
            return render(request, 'login_form.html', {'error_message': 'Invalid credentials'})
    else:
        # Render the login page
        return render(request, 'login_form.html')

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
