from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm 

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            users = authenticate(username=username, password=password)
            if users is not None:
                login(request,users)  # this makes the users automatically login after the registration is complete..
            messages.success(request, f'Your account has been created for {username}! You are now able to log in')
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'user/signup.html',{"form":form})

def home(request):
    return render(request,'user/home.html')


@ login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileForm(request.POST,instance=request.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        p_form = ProfileForm(instance=request.user)

    context = {
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)