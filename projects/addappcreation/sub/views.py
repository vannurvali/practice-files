from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'sub.html')

def sub_cal(request):
    dict1 = request.GET
    num1 = int(dict1['num1'])
    num2 = int(dict1['num2'])
    return render(request,'sub.html',{'res':num1-num2})