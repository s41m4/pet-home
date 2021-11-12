from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from home.decorators import unauthenticated_user
from rest_framework import viewsets
from .serializers import *
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