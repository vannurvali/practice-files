# familymembers/addfamilymember


from django.urls import path
from FamilyMembers.views import *

urlpatterns = [
    path('addfamilymember',addmemberpage),
    path('savedata',savedata),
    path('retrive-records',retrive_records),
    path('update_user/<int:id>',update_user),
    path('delete_user/int:id>',delete_user)
]