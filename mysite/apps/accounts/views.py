from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
import re


def login(request):
    pass


def register(request):
    # if request.method == 'POST':
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['pass']
    password2 = request.POST['pass2']

    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print('Email is not valid!')
    elif password != password2:
        print('The passwords do not match!')
    else:
        user = User.objects.create_user(username=user, password=password1, email=email)
        user.save()
        print('A new user registered!')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


