from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class MP_serializer(serializers.ModelSerializer):

    class Meta:
        model = MP_files
        fields = "__all__"