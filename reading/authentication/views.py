from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,"registration/success.html", {})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.get("username") 
            password = form.get("password")
            messages.success(req, f'Welcome, {username}!')
            return redirect('library-home')
        else:
            form = UserSignupForm()
        data = {'form': form}
    return render(req, 'users/signup.html', data)