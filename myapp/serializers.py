from django.forms import models
from rest_framework import serializers
from .models import ticket

class ticketserializer(serializers.ModelSerializer):
    class Meta:
        model=ticket
        fields=['title','body','username1']
