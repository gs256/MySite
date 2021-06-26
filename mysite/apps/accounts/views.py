from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
import re


def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


def login(request):
    username = request.POST['username']
    password = request.POST['pass']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        print('Authentication error')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def register(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['pass']
    password2 = request.POST['pass2']

    # Check if email is correct
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print('Email is not valid!')
    elif password != password2:
        print('The passwords do not match!')
    elif User.objects.filter(username=username).exists():
        print('The username is already taken')
    elif User.objects.filter(email=email).exists():
        print('The email is already taken')
    else:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('A new user is registered!')
        return HttpResponseRedirect(reverse('accounts:profile'))
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


