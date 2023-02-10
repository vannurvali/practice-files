from django.urls import path
from sub.views import sub

urlpatterns = [
    path('sendaddmessage',sub)

]