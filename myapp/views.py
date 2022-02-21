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
from time import strftime
from django.views.decorators.csrf import csrf_exempt
from .serializers import ticketserializer
from rest_framework.parsers import JSONParser
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
            print('###############time is',datetime.now().strftime("%Y-%m-%d,%H:%M:%S"))
            k.date=datetime.now().strftime("%m-%d, %H:%M:%S")
            k.save()
    p=ticket.objects.filter(username1=user_is)
    print('p is',p)
    return render(request,'inside.html',{'p':p,'fname':user_is})

def signin(request):
    if request.method=='POST':
        uname=request.POST['username3']
        pwd=request.POST['password3']
        User=authenticate(username=uname,password= pwd)
        print('##############################user is',User)
        if(User=='admin'):
            p=ticket.objects.all()
            return render(request,'inside2.html',{'p':p,'fname':User})
        elif User is not None:
            p=ticket.objects.filter(username1=User)
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

@csrf_exempt                                                    #not required for  GET request
def ticketlist(request):
    print('########################insideticketlist1')
    if request.method=='GET':
        print('########################insideticketlist2')
        #articleobjects=article.objects.Get()
        #articleserilized=articleserializer(articleobjects)  if one object many=true is not needed
        ticketobjects=ticket.objects.all()
        ticketserilized=ticketserializer(ticketobjects,many=True)
        return JsonResponse(ticketserilized.data,safe=False)
    elif request.method=='POST':
        print('########################insideticketlist3')
        data=JSONParser().parse(request)
        ticketserilized=ticketserializer(data=data)
        if ticketserilized.is_valid():
            print('########################insideticketlist4')
            ticketserilized.save()
            return JsonResponse(ticketserilized.data,status=201)
        return JsonResponse(ticketserilized.errors,status=400)

@csrf_exempt
def ticketdetail(request,input1):
    print('########################insideticketlist5')
    try:
        ticketobjects=ticket.objects.get(title=input1)
    except:
        return HttpResponse(status=404)
    if request.method=='GET':
        print('########################insideticketlist6')
        ticketserilized=ticketserializer(ticketobjects)
        return JsonResponse(ticketserilized.data,safe=False)
    elif request.method=='PUT':
        print('########################insideticketlist7')
        data=JSONParser().parse(request)
        ticketserilized=ticketserializer(ticketobjects,data=data)
        if ticketserilized.is_valid():
            ticketserilized.save()
            return JsonResponse(ticketserilized.data)
        return JsonResponse(ticketserilized.errors,status=400)
    elif request.method =='DELETE':
        ticketobjects.delete()
        return HttpResponse(status=204)    