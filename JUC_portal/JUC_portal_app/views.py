import re
from django.shortcuts import render
from .forms import StudentModelForm
from .forms import BlogModelForm
from django.shortcuts import render,redirect,resolve_url
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import BlogPost
# Create your views here.
def home (request):
    blog=BlogPost.objects.all()
    return (
        render(request,'home.html',{'blog':blog})  #to return a templete
    )

def newStudent(request):
    form=StudentModelForm()
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account have been created successfully, please sign in '+form.cleaned_data.get('username'))

            return redirect('/login')

    context={'form':form}
    return render(request,'signup.html',context)  

def login(request):
    form=StudentModelForm()
    if request.method=='POST':
        #login user
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('')
        else:
            messages.info(request,'Username or password is incorrect')
    context={'form':form}
    return render(request,'login.html',context)

def writeBlog(request):
    form=BlogModelForm()
    if request.method=='POST':
        form=BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Done !!')

            # return redirect('/login')
    return (
        render(request,'write.html',{'form':form})  #to return a templete
    )


    #     username=request.POST['username']
    #     password= request.POST['password']
    #     print('username: ',username,'password: ',password)
    #     user=authenticate(request,username=username,password=password)
    #     if user is not None:
    #         messages.info(request,'Username is correct')    
    #         login(request,user)
    #         return redirect('/signup')
    #     else:
    #         messages.info(request,'Username or password is incorrect')    
    # return render(request,'login.html',{'form':form})