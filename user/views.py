from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            users = authenticate(username=username, password=password)
            
            messages.success(request, f'Your account has been created for {username}! You are now able to log in')
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'user/signup.html',{"form":form})

def home(request):
    return render(request,'user/home.html')



    
