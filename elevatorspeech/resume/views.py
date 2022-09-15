from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest
from .forms import *
from .models import *


# Create your views here.

def home(request: HttpRequest):
    data = resumes.objects.all()
    return render(request, 'resume/index.html', {'resumes': data})


def about(request: HttpRequest):
    return render(request, 'resume/about.html')


def addResume(request: HttpRequest):
    if request.method == 'POST':
        form = AddResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('resume:home'))
        else:
            msg = 'Your input is too long description'
            return render(request, 'resume/add_resume.html', {'msg': msg})
    form = AddResumeForm()
    return render(request, 'resume/add_resume.html', {'form': form})
