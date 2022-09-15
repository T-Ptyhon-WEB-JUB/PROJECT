from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest
from .forms import *
from .models import *


# Create your views here.

def home(request: HttpRequest):
    data = resumes.objects.all().order_by('created_data')
    return render(request, 'resume/index.html', {'resumes': data})


def about(request: HttpRequest):
    return render(request, 'resume/about.html')


def addResume(request: HttpRequest):
    if request.method == 'POST':
        form = AddResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('resume:home'))
        else:
            msg = 'Please check your input'
            return render(request, 'resume/add_resume.html', {'msg': msg})
    form = AddResumeForm()
    return render(request, 'resume/add_resume.html', {'form': form})
