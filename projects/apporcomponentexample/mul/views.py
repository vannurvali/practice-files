from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mul(request):
    return HttpResponse("welcome to mul")