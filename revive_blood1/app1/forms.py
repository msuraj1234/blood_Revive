from django import forms
from django.db import models
from django import forms
from .models import suggestion

class SuggestForm(forms.ModelForm):
    class Meta:
        model = suggestion
        fields = '__all__'
        labels = {'others':'Suggest','name1':'Name'}