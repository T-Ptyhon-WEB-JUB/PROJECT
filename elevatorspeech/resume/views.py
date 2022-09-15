from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest


# Create your views here.

def home(request: HttpRequest):
    return render(request, 'resume/index.html')
