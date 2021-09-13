from django import forms
from .models import *
class contactform(forms.Form):
    YOURFIRSTNAME=forms.CharField(max_length=70)
    YOURLASTNAME=forms.CharField(max_length=70)
    YOUREMAIL=forms.EmailField(max_length=70)
    YOURMESSAGEFORUS =forms.CharField(max_length=70,widget=forms.Textarea)

class Blood_donor_form(forms.ModelForm):
    class Meta:
        model=Blood_donor_model
        fields='__all__'
        labels={'Unitsofbloodrequried':'Units of blood required','PatientBloodGroup':'Patient BloodGroup','PatientAge':'Patient Age',
                'PhoneNumber':'Phone Number','HospitalName':'Hospital Name'}

        widgets = { 'Name':forms.TextInput(attrs={ 'pattern': '[A-Za-z ]+','title': 'Enter Characters Only '}),
                    'Email': forms.TextInput(attrs={'placeholder': 'xyz@gmail.com'}),
                   }