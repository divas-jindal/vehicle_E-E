from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from register.models import fac
from . import models
from django.shortcuts import render,redirect
import datetime

def registerfacVehicle(request):
    if request.method == 'POST':
        obj = fac()
        print("jhgbu")
        obj.name = request.POST["name"]
        obj.vehicle_no = request.POST["vehicle_no"]
        obj.vehicle_type = request.POST["type"]
        obj.des = request.POST["des"]
        obj.in_out= request.POST["in_out"]
        time = datetime.datetime.now()
        obj.time= time
        print("jhgbu")
        obj.save()
        return redirect('/')
    return render(request,'register/register_base.html')

def veh(request):

    try:
         obj = fac.objects.get(vehicle_no=request.POST["vehno"])
         return render(request,'register/register_base.html',{"obj":obj})
         # return render('/register')
        # return redirect('/')
        #fac.objects.filter(vehicle_no=request.POST["vehno"])
        #   return redirect('/register')
    except:
        return redirect('/groups')
