from django.urls import path
from add.views import add


urlpatterns = [
    path('',add)

]