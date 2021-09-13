from django import forms
from .models import Donor_mdl

choice = (('male', 'Male'),
          ('Female', 'Female'),
          ('Other', 'Other'),)

SAMPLE_CHOICES = (('BP', 'BP'), ('Diabetes', 'Diabetes'), ('Smoking', 'Smoking'), ('Alcoholic', 'Alcoholic'),('None','None'))



class Donor_frm(forms.ModelForm):
    extra_info = forms.MultipleChoiceField(choices=SAMPLE_CHOICES, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Donor_mdl
        exclude = ['donation_id']
        labels={'date_brth':'Date_Birth'}
        widgets = {
            'name': forms.TextInput(attrs={'class': "inputfrms",'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only ',
                                           'placeholder': 'Enter Your Name'}),
            'fname': forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only ','placeholder': 'Enter Your father name '}),
            'Gender': forms.RadioSelect(choices=choice),
            'Address': forms.TextInput(attrs={'placeholder': 'area'}),
            'age': forms.TextInput(attrs={'placeholder': 'above 16 years only'}),
            'date_brth': forms.TextInput(attrs={'type': 'date'}),
            'Email': forms.TextInput(attrs={'placeholder': 'xyz@gmail.com'}),
            'LastDonateDate': forms.TextInput(attrs={'type': 'date'}),
        }