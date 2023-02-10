from django.shortcuts import render


def add(request):
    return render(request,'add.html')

def sub(request):
    return render(request,'sub.html')

def mul(request):
    return render(request,'mul.html')