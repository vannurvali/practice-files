from django.shortcuts import render


# render : used to send html pages to the user
def send_html(request):
    return render(request,'home.html')


# server not able to find where the htmlfile is located

# base dir/sendhtmlpage