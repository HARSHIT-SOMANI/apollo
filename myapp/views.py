from telnetlib import STATUS
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from .models import uploads,article
#from .serializers import articleserializer,uploadserializer
#from rest_framework.parsers import JSONParser
#from django.views.decorators.csrf import csrf_exempt
import json



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

def signin(request):
    #print('#####in sinin function')
    if request.method=='POST':
        #print('#####in sinin function222')
        uname=request.POST['username3']
        pwd=request.POST['password3']
        User=authenticate(username=uname,password= pwd)
        #print('user is',User)
        #p=uploads.objects.all()
        if User is not None:
            #print('#####in sinin function33333')
            #login(request,User)
            #print('******sinin function5555555')
            return render(request,'inside.html',{'fname':User})
        else:
            print('#####in sinin function4444')
            messages.info(request,'wrong password')
            return redirect('signind')
    #y=uploads.objects.all()    
    #print('in sinin function2')
    return render(request,'signin.html')


def signout(request):
    logout(request)
    return redirect('indexd')