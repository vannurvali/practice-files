from django.urls import path
from Userapp.views import *


urlpatterns =[
    path('',register),
    path('register-user',register_user),
    path('login-user',login_user),
    path('send',send)


]