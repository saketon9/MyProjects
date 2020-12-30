from django import forms
from django.forms import ModelForm
from .models import *


class reviewForm(forms.ModelForm):
    class Meta:
        model = company_Reviews
        fields = '__all__'
