from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from groups.models import Guest
from . import models
from django.shortcuts import render,redirect
import datetime


def registerVehicle(request):
    if request.method == 'POST':
        obj = Guest()
        obj.name = request.POST["name"]
        obj.vehicle_no = request.POST["vehicle_no"]
        obj.vehicle_type = request.POST["type"]
        obj.purpose = request.POST["purpose"]
        obj.in_out= request.POST["in_out"]
        time = datetime.datetime.now()
        obj.time = time

        obj.save()
        return redirect('/')
    return render(request,'groups/group_base.html')
