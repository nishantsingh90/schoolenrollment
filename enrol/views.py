from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework import filters
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from datetime import datetime
from django.utils import timezone


class CityAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class =CitySerializer


class GradeAPIView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class =GradeSerializer

class PinAPIView(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class =PinSerializer







def index(request):
    stu=Student.objects.all()
    return render(request,"index.html",{'students':stu})





b=[]
def validatemobile(request):
    if request.is_ajax():
        amount=request.POST.get('amount')
        if amount.isdigit():
            a=[0,1,2,3,4,5]
            if int(amount[0]) in a:
                amount=""
                b.clear()
                b.append(amount)
            elif len (amount)>10:
                amount=""
                b.clear()
                b.append(amount)


            else:
                amount=amount
                b.clear()
                b.append(amount)

        else:
            amount=""
            b.clear()
            b.append(amount)

        response = {
                         'amount':b[0]
            }
        return JsonResponse(response)

from django.core import serializers
from django.http import HttpResponse
p=[]
def findpincode(request):


    if request.is_ajax() and request.method == "POST":

        amount=request.POST.get('amount')
        print(amount)
        if len(amount)>3:
            pin=Pin.objects.filter(pincode__startswith=amount)
            p.clear()


            p.append(pin)
    result=p[0]

    serializer=PinSerializer(result,many=True)

    return JsonResponse(serializer.data,safe=False)



def studentform(request):
    if request.is_ajax():
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        email=request.POST.get('email')
        grade=request.POST.get('grade')
        marks=request.POST.get('marks')
        dob=request.POST.get('dob')
        if len(city)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(name)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(fname)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(address)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(mobile)<10:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(email)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(pincode)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(dob)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(grade)==0:
            stu=Student.objects.get(name="QWSDFRTVG")
        if not(marks.isdigit()):
            stu=Student.objects.get(name="QWSDFRTVG")
        if not "@" in email:
            stu=Student.objects.get(name="QWSDFRTVG")

        date=datetime.strptime(dob, "%Y-%m-%d")
        time=timezone.now()


        student=Student.objects.create(name=name,fathers_name=fname,dob=date,address=address,city=city,pin=pincode,email=email,mobile=mobile,std=grade,marks=marks,time=time)
        id1=student.id
        response = {
                         'amount':id1
            }
        return JsonResponse(response)
def studentform1(request):
    if request.is_ajax():
        id1=request.POST.get('id1')
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        email=request.POST.get('email')
        grade=request.POST.get('grade')
        marks=request.POST.get('marks')
        dob=request.POST.get('dob')
        if len(city)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(name)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(fname)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(address)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(mobile)<10:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(email)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(pincode)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(dob)<3:
            stu=Student.objects.get(name="QWSDFRTVG")
        if len(grade)==0:
            stu=Student.objects.get(name="QWSDFRTVG")
        if not(marks.isdigit()):
            stu=Student.objects.get(name="QWSDFRTVG")
        if not "@" in email:
            stu=Student.objects.get(name="QWSDFRTVG")

        date=datetime.strptime(dob, "%Y-%m-%d")
        time=timezone.now()
        student=Student.objects.get(id=id1)
        student.name=name
        student.fathers_name=fname
        student.dob=dob
        student.address=address
        student.city=city
        student.pin=pincode
        student.email=email
        student.mobile=mobile
        student.std=grade
        student.marks=marks
        response = {
                         'amount':id1
            }
        return JsonResponse(response)

def showstudent(request):
    if request.is_ajax():
        id1=request.POST.get('id1')
        stu=Student.objects.get(id=id1)
        name=stu.name
        fname=stu.fathers_name
        dob=stu.dob
        address=stu.address
        city=stu.city
        pin=stu.pin
        email=stu.email
        mobile=stu.mobile
        std=stu.std
        marks=stu.marks
        response = {
                         'name':name,'fname':fname,'dob':dob,'address':address,'city':city,'pin':pin,'email':email,'mobile':mobile,'std':std,'marks':marks,
            }
        return JsonResponse(response)

def editstudent(request):
    if request.is_ajax():
        id1=request.POST.get('id1')
        stu=Student.objects.get(id=id1)
        name=stu.name
        fname=stu.fathers_name
        dob=stu.dob
        address=stu.address
        city=stu.city
        pin=stu.pin
        email=stu.email
        mobile=stu.mobile
        std=stu.std
        marks=stu.marks
        response = {
                         'id1':id1,'name':name,'fname':fname,'dob':dob,'address':address,'city':city,'pin':pin,'email':email,'mobile':mobile,'std':std,'marks':marks,
            }
        return JsonResponse(response)



