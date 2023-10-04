from django.shortcuts import render
from django.http import HttpResponse
from registration.models import form
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        print(first_name)
        last_name=request.POST['last_name']
        print(last_name)
        email_ID=request.POST['email_ID']
        print(email_ID)
        user=form(first_name=first_name,last_name=last_name,mail_ID=email_ID)
        user.save() 
        return render(request,'register.html')
        # print("details saved")
    else:
        return render(request,'home.html')


def register(request):
    return render(request,'register.html')

def log_in(request):
    user_name=request.POST['user_name']
    password=request.POST['password']
    if(first_name==user_name and password==password):
        login=form2(user_name=user_name,password=password)
        return render(request,'log_in.html')

def welcome(request):
    return render(request,'welcome.html')
    

# def user_info(request):
    
