from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Userapp.models import Sample

# Create your views here.


def register(request):
    return render(request,'home.html')

def register_user(request):
    dict1 = request.POST
    username = dict1['username']
    password = dict1['password']
    email = dict1['email']
    user = User.objects.create_user(username,email=email,password=password)
    user.save()
    # return redirect('/')
    return render(request,'login.html')

def login_user(request):
    dict1 = request.POST
    username = dict1['username']
    password = dict1['password']
    user = authenticate(username=username,password=password)
    if user is None:
        return render(request,'login.html')
    else:
        login(request,user)
        return render(request,'sample.html')
    # return HttpResponse(user)

def send(request):
    # res = request.user
    logout(request)
    # return HttpResponse(request.user)
    return render(request,'sample.html')


