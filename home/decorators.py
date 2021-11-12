from django.contrib.auth import decorators
from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_admin:
                return redirect('admin')
            else:
                return redirect('index')
        return wrapper_func
    return decorator