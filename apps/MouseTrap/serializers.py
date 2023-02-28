from rest_framework import serializers
from .models import *  # Update the model name from PictureSensor to MouseTrap

class RatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rats
        fields = ['id', 'name', 'description']

class MouseTrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MouseTrap
        fields = ['id', 'image', 'rats', 'created_by', 'created_at']

class MouseTrap2Serializer(serializers.ModelSerializer):
    class Meta:
        model = MouseTrap2
        fields = ['id', 'image','created_at']