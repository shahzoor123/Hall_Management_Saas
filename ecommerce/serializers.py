from rest_framework import serializers
from .models import Event  # Make sure to import the Event model from your models.py

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'