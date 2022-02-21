from datetime import date,datetime
from time import time
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
        


