from django.db import models

class Donor_mdl(models.Model):
    c = (
        ('Hyderabad','Hyderabad'),
    )
    donation_id = models.IntegerField(null=True)
    name = models.CharField(max_length=30, null=True)
    fname = models.CharField(max_length=30, null=True)
    blood_group = models.CharField(choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'),
                                            ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=50)
    age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=10, null=True)
    date_brth = models.DateField(null=True)
    email = models.EmailField(null=True, help_text ='xyz@gmail.com')
    address = models.CharField(max_length=50, null=True, help_text ='Area')
    city = models.CharField(max_length=50, default='Hyderabad',choices = c)
    phone_no = models.IntegerField()
    LastDonateDate = models.DateField(null=True)
    extra_info = models.CharField(max_length=50)
