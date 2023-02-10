from django.urls import path
from sub.views import home,sub_cal

urlpatterns = [
    path('',home),
    path('hai',sub_cal)


]