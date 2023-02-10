from django.urls import path
from userdata.views import home,save_user



urlpatterns = [
    path('',home),
    path('save',save_user)


]