from django.db import models

# Create your models here.
#from phonenumber_field.modelfields import PhoneNumberField



class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    mobile = models.IntegerField()
    password = models.CharField(max_length=18)
    repeat_password = models.CharField(max_length=18)


class Login(models.Model):
    email_id = models.EmailField(max_length=60)
    password = models.CharField(max_length=10)






