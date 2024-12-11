from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
 

# Login View 
from django.db import IntegrityError
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Contactfrom django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact  

#County
from .forms import County
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Error messages placeholder
        error_message = None

        # Check if the user exists
        user_exists = User.objects.filter(username=username).exists()

        if not user_exists:
            error_message = "Account does not exist. Please sign up."
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my_home')  # Change 'my_home' to your target view name
            else:
                error_message = "Incorrect password. Please try again."

        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


# Sign Up View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Your account has been successfully created")
                return redirect('login')
            except IntegrityError:
                error_message = "Username already exists"
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = "Passwords do not match"
            return render(request, 'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')

# Home View
@login_required
def home(request):
    return render(request, 'index.html')

# Seasons View
@login_required
def seasons(request):
    return render(request, 'seasons.html')

# Product View
@login_required
def product(request):
    return render(request, 'product.html')

# Cereals View
@login_required
def cereals(request):
    return render(request, 'cereals.html')

# Beverage View
@login_required
def beverage(request):
    return render(request, 'beverage.html')

# Fruits View
@login_required
def fruits(request):
    return render(request, 'fruits.html')

# Vegetables View
@login_required
def vegetables(request):
    return render(request, 'vegetables.html')

# Legumes View
@login_required
def legumes(request):
    return render(request, 'legumes.html')

# Contact View
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This will save to the database
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})



@login_required
@csrf_exempt
def submit_county(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        county = request.POST.get('county')

        try:
            # Create a new entry regardless of duplicates
            County.objects.create(name=name, county=county)
            return JsonResponse({
                'success': True,
                'message': 'County information submitted successfully!'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'An error occurred: {e}'
            })

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})