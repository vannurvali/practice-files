from django.urls import path
from add.views import home,add_res


urlpatterns = [
    path('',home),
    path('hello',add_res)

]