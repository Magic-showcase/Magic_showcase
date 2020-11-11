
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def Login(request):
    if request.method == 'POST'
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
