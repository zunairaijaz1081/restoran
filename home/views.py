from home.models import Contact
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Reservation  
from django.core.files.storage import FileSystemStorage
from .models import User_profile
from django.conf import settings
from django.contrib.auth import get_backends
        
#Home Page

def index(request):
    """Render the home page."""
    return render(request, 'index.html')




# About page
def about(request):
    return render(request, "about.html")



#Services page

def services(request):
    return render(request, "services.html")






# menu page

def menu(request):
    return render(request, "menu.html")









from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, get_backends
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)

        # ✅ Fix: Set backend explicitly
        backend = get_backends()[0]
        user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

        auth_login(request, user)
        messages.success(request, "Signup successful!")
        return redirect('index')

    return render(request, 'register.html')






#Login page

def login(request):

    if request.user is not None:
        if request.user.is_authenticated:
            return redirect('index')


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user = get_object_or_404(username=username, password=password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')








#contact page request


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')







from django.shortcuts import render
from .models import Reservation
from datetime import datetime

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        datetime_str = request.POST.get('datetime')
        number_of_people = request.POST.get('number_of_people')
        special_request = request.POST.get('special_request')

        try:
            date_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M").date()
        except ValueError:
            return render(request, 'index.html', {'error': 'Invalid date format'})

        Reservation.objects.create(
            name=name,
            email=email,
            date=date_obj,
            number_of_people=number_of_people,
            special_request=special_request
        )

        return render(request, 'booking.html', {'success': True})

    return render(request, 'booking.html')










#login required for logout

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')




#login required for profile_picture

@login_required
def profile_picture(request):


    # Get the user's profile or create one if it doesn't exist
    user_profile, created = User_profile.objects.get_or_create(user=request.user)

    if request.method == 'POST' and request.FILES['profile_picture']:
        uploaded_file = request.FILES['profile_picture']
        try:
            # Save the file to the default media directory
            #fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            #filename = fs.save(uploaded_file.name, uploaded_file)

            # Update the profile picture
            user_profile.profile_picture = uploaded_file
            user_profile.save()

            return redirect('index')  # Redirect to show updated profile picture
        except Exception as e:
            # Return error if there is an issue
            return JsonResponse({'status': 'error', 'message': str(e)})

    return render(request, 'index.html') 

















from django.shortcuts import render
from .models import MenuItem

def menu(request):
    breakfast_items = MenuItem.objects.filter(category='breakfast')
    lunch_items = MenuItem.objects.filter(category='lunch')
    dinner_items = MenuItem.objects.filter(category='dinner')

    context = {
        'breakfast_items': breakfast_items,
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
    }
    return render(request, 'menu.html', context)




from django.shortcuts import render
from .models import Chef

from .models import Chef

def index(request):
    chefs = Chef.objects.all()
    return render(request, 'index.html', {'chefs': chefs})

from django.shortcuts import redirect, render
from django.contrib import messages

def profile_picture(request):
    if request.method == 'POST':
        if 'profile_picture' in request.FILES:
            profile_pic = request.FILES['profile_picture']
            user_profile = request.user.user_profile
            user_profile.profile_picture = profile_pic
            user_profile.save()
            messages.success(request, "Profile picture updated successfully!")
        else:
            messages.error(request, "No profile picture chosen.")
        return redirect('index')  # Or wherever you want to redirect after POST
    
    # For GET or other methods, render some template or redirect
    return redirect('index')  # Or render a form page if you have one
