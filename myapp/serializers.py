from django.forms import models
from rest_framework import serializers
from .models import ticket,ticket_response

class ticketserializer(serializers.ModelSerializer):
    class Meta:
        model=ticket
        fields=['title','body','username1']

class ticket_responseserializer(serializers.ModelSerializer):
    class Meta:
        model=ticket_response
        fields=['status','remarks']


