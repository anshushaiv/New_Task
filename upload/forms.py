from dataclasses import fields
from pyexpat import model
from .models import *
from django import forms


class MP_forms(forms.ModelForm):

    class Meta:
        model = MP_files
        fields = "__all__"
