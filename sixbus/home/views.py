from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
from django.views.generic import TemplateView
import datetime
from .forms import addressForm1
from .forms import addressForm2
from .models import bus1
from .models import bus2


# Create your views here.


def home(request: HttpRequest):
    b1 = bus1.objects.all()
    b2 = bus2.objects.all()
    return render(request, 'home/index.html', {"bus1": b1 ,"bus2": b2 })


def add_bus1(request: HttpRequest):
    if request.method == "POST":
        new_addresss = addressForm1(request.POST)
        if new_addresss.is_valid():
            new_addresss.save()
            return redirect(resolve_url("home:index"))
    new_addresss = addressForm1()
    return render(request, 'home/add.html', {"form": new_addresss})



def add_bus2(request: HttpRequest):
    if request.method == "POST":
        new_addresss = addressForm2(request.POST)
        if new_addresss.is_valid():
            new_addresss.save()
            return redirect(resolve_url("home:index"))
    new_addresss = addressForm2()
    return render(request, 'home/add2.html', {"form": new_addresss})


def v(request: HttpRequest):
    b1 = bus1.objects.all()
    b2 = bus2.objects.all()
    return render(request, 'home/support.html', {"bus1": b1, "bus2": b2})