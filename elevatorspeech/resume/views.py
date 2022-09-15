from django.shortcuts import render, redirect, resolve_url


# Create your views here.

def home(request):
    return render(request, 'resume/index.html')
