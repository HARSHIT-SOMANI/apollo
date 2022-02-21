from datetime import date
from time import time
from django.db import models

# Create your models here.

class uploads(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=500)
    username1=models.CharField(max_length=100,default=None,null=True)
    date=models.TimeField(auto_now_add=True)
