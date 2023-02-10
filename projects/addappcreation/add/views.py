from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'add.html')

def add_res(request):
    dict1 = request.GET
    num1 = int(dict1['num1'])
    num2 = int(dict1['num2'])
    return render(request,'add.html',{'res':num1+num2})