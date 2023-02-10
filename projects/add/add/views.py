from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    return render(request,'add.html')

def  add_name(request):
    dict1= request.GET
    num1 = int(dict1['num1'])
    num2 = int(dict1['num2'])
    res = num1 + num2
    print(res)
    return render(request,'out.html',{'out':res})

#basedic/templates