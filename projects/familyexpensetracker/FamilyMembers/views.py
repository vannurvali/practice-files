from django.shortcuts import render,redirect
from FamilyMembers.models import FamilyMember
from django.contrib import messages
from FamilyMembers.validators import sample,validate_file_size
# Create your views here.


def addmemberpage(request):
    return render(request,'addmember.html')

def savedata(request):
    dict1 = request.POST
    images = request.FILES
    name = dict1['name']
    mobile = dict1['mobile']
    work = dict1['work']
    income = dict1['income']
    Profile_image = images['image']
    obj = FamilyMember()
    obj.name = name
    obj.work = work
    obj.mobile = mobile
    obj.income = income
    obj.profile_image = prof_image
    obj.pay_slip = images['payslip']
    obj.save()
    return redirect('/')

def retrive_records(request):
    objects = FamilyMember.objects.all()
    return render(request,'records.html',{'data':objects})

def update_user(request,id):
    det = FamilyMember.objects.get(id = id)
    # print(det)
    return render(request,'update_user.html',{'det':det})

def updated_user(request,id):
    dict1 = request.POST
    mobile = dict1['mobile']
    work = dict1['work']
    income = dict1['income']
    det = FamilyMember.objects.get(id=id)
    det.mobile = mobile
    det.income = income
    det.work = work
    det.save()
    # return redirect('/familymembers/retrive_records')
    return redirect('/')

def delete_user(request,id):
    det = FamilyMember.objects.get(id=id)
    det.delete()
    return redirect('/familymembers/retrive_records')



