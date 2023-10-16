from rest_framework import serializers
from .models import *
class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'