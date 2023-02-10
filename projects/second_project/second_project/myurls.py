from django.urls import path
from.views import home, show_greet


urlpatterns =[
    path('', home),
    path('getdata', show_greet)

]