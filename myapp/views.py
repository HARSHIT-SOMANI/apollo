#super user ,useid:admin pwd:1

import imp
from telnetlib import STATUS
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import ticket
from datetime import datetime
#from .serializers import articleserializer,uploadserializer
#from rest_framework.parsers import JSONParser
#from django.views.decorators.csrf import csrf_exempt
import json

from myapp.models import ticket



def index(request):
    #print('******index function')
    return render(request,'index.html')

def signup(request):
    print('######cvme to sinup')
    if request.method=='POST':
        print('######cvme to sinup1')
        username=request.POST['username']
        lastname=request.POST['lastname']
        firstname=request.POST['firstname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(User.objects.filter(username=username).exists()):
            print('########################username exits')
            messages.info(request,'Username taken')
            return redirect('signupd')
        elif(User.objects.filter(email=email)):
            print('########################emil exits')
            messages.info(request,'email taken')
            return redirect('signupd')
        else:
            print('########################nothin exists')
            myuser=User.objects.create_user(username,email,password1)
            myuser.firstname=firstname
            myuser.lastname=lastname
            myuser.save()
            messages.info(request,'account created')
            return redirect('signind')
    return render(request,'signup.html')


def fileread(request):
    user_is=request.POST['username']
    if request.method=='POST':
            k=ticket.objects.create(title=request.POST['title'])
            k.body=request.POST['body']
            k.username1=user_is
            k.save()
    p=ticket.objects.filter(username1=user_is)
    print('p is',p)
    return render(request,'inside.html',{'p':p,'fname':user_is})

def signin(request):
    if request.method=='POST':
        uname=request.POST['username3']
        pwd=request.POST['password3']
        User=authenticate(username=uname,password= pwd)
        p=ticket.objects.filter(username1=User)
        if User is not None:
            return render(request,'inside.html',{'p':p,'fname':User})
        else:
            messages.info(request,'wrong password')
            return redirect('signind')
    #y=uploads.objects.all()    
    #print('in sinin function2')
    return render(request,'signin.html')


def signout(request):
    logout(request)
    return redirect('indexd')