from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    return render (request,"add.html")


def two_words(request):
    dict1 = request.GET
    return render(request,'out.html',{'out':dict1})