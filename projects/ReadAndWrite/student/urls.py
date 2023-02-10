from django.urls import path
from student.views import *

urlpatterns = [
    path('register',register_page),
    path('registeruser',register_user),
    path('records',get_records),
    path('univsearch',send_search_univ),
    path('getresultsbaseduniv',getunivresults),
    path('branchsearch',send_branch_search),
    path('getresultsbasedbranch',getbranchresults)

    # student/register
    # path('getstudentrecords',register_page)

]

