from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def show_greet(request):
    dict1 = request.GET
    name = dict1['in1']
    return render(request,'home.html',{'name': name})
