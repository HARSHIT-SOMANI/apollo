from datetime import date,datetime
from time import time
from tkinter import CASCADE
from django.db import models

# Create your models here.

class ticket(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=500)
    username1=models.CharField(max_length=100,default=None,null=True)
    date=models.CharField(max_length=500)
    #date=models.DateTimeField(default=datetime.now)
    #status=models.CharField(default='TO-DO',max_length=50)
    #remarks=models.CharField(default='Na',null=True,max_length=200)
    #date2=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title

class ticket_response(models.Model):
    status=models.CharField(max_length=50,default='To do')
    remarks=models.CharField(max_length=500)
    date=models.CharField(max_length=500)
    ticketid=models.ForeignKey(ticket,on_delete=models.CASCADE)
    def __str__(self):
        return self.status 
        


