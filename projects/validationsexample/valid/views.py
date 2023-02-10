from django.shortcuts import render,redirect
from valid.validations import phone_validation,email_validation,file_validation
from django.core.exceptions import ValidationError
from valid.models import Sample
# Create your views here.

def home(request):
    return render(request,'home.html')

def submitdata(request):
    dict1 = request.POST
    images_dict = request.FILES
    phone = dict1['phone']
    email = dict1['email']
    image = images_dict['pic']
    try:
        phone_validation(phone)
    except ValidationError :
        return render(request,'home.html',{'phoneerror':'your number should in the format +91-xxxxxxxxxx'})
    try:
        email_validation(email)
    except ValidationError :
        return render(request,'home.html',{'phoneerror':'your email should contain @'})
    try:
        file_validation(image)
    except ValidationError :
        return render(request,'home.html',{'phoneerror':'your file should be greater than 50kb and less 100kb'})
    s = Sample()
    s.email = email
    s.phone_number = phone
    s.pic = image
    s.save()



    return redirect('/')
