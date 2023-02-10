from django.shortcuts import render,redirect
from trainee.models import Trainee
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'register.html')

def save_method(request):
    dict1 = request.POST
    name = dict1['username']
    regid = int(dict1['regid'])
    phone_number = int(dict1['phonenumber'])
    subject = dict1['subject']
    obj = Trainee()
    obj.trainee_name = name
    obj.reg_id = regid
    obj.phone_number = phone_number
    obj.subject = subject
    obj.save()
    return redirect('/register')



