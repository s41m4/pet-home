from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from home.decorators import unauthenticated_user
from rest_framework import viewsets
from .serializers import *
from .models import Pet
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from .forms import *
from datetime import date, datetime
import calendar
from django.db.models import Sum
from rest_framework.decorators import api_view
import dateutil.relativedelta

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            messages.warning(request, "L'identifiant et/ou le mot de passe est incorrect")

    context = {}
    return render(request, 'home/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'home/index.html')


def error_404(request, exception):
        return render(request,'home/404.html')

def default_map(request):
    return render(request, 'home/index.html', {})

#@unauthenticated_user
def signup(request):
       if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
        else:
            user_form = UserCreationForm()
            profile_form = ProfileForm()
        return render(request, 'home/signup.html', {
            'user_form': user_form,
            'profile_form': profile_form
    })

@login_required(login_url='login')
def users(request):
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'home/users.html', context)

@login_required(login_url='login')
def announcement(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home/announcement.html', context)

@login_required(login_url='login')
def add_announcement(request):
    context = {}
    return render(request, 'home/add_announcement.html', context)

@login_required(login_url='login')
def user_profile(request):
    customer = Profile.objects.get
    context = {'customer':customer}
    return render(request, 'home/user_profile.html',context)

@login_required(login_url='login')
def updateUser(request):
    profile = Profile.objects.get
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"le profil de {profile.user.first_name} {profile.user.last_name} est mis à jour avec succés!")
            return redirect('users')
    else:
        form = ProfileForm(instance=profile)
    context = {'form':form}
    return render(request, 'home/user_form.html', context)

@login_required(login_url='login')
def deleteUser(request, pk):
    user = Profile.objects.get(user_id=pk)
    if request.method == 'POST':
        user.delete()
        messages.warning(request, "Pet deleted with success!!")
        return redirect('users')
        
    context = {'item':user}
    return render(request, 'home/delete_user.html', context)
