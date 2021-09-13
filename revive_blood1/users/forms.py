from django import forms
from .models import Signup
from .models import Login


class Signup_form(forms.ModelForm):

    class Meta:
        model = Signup
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class Login_form(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'
        widgets ={
            'password':forms.PasswordInput()
        }



