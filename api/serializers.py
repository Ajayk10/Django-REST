from rest_framework.fields import SerializerMethodField

from .models import *
from rest_framework.serializers import ModelSerializer

class JobSerializer(ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
