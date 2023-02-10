from django.http import HttpResponse

#Http Response
def say_hello_world(request):
    return HttpResponse ("hello world")

def say_bye(request):
    return HttpResponse ("bye")

def say_welcome(request):
    return HttpResponse (" <h1> hello user welcome to my website <h1> ")

def say_massy(request):
    return HttpResponse ("massy")