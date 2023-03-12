from rest_framework import serializers
from .models import * 

class SMALLSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMALLS
        fields = '__all__'