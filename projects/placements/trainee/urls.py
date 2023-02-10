from django.urls import path
from trainee.views import home,save_method


urlpatterns = [
    path('',home),
    path('save',save_method)

]