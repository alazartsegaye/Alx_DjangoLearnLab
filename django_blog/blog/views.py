from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('profile')  # Redirect to profile page
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login View (using Django's built-in view)
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    authentication_form = AuthenticationForm

# Logout View (using Django's built-in view)
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

# Profile Management View
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})