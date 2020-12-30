from django import forms
from django.forms import ModelForm
from .models import *


class todo_app(forms.ModelForm):
    class Meta:
        model = todoList
        fields = '__all__'
