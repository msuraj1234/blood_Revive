from django.db import models

# Create your models here.
class Blood_donor_model(models.Model):
  CHOICES1 = (('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'),
                           ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+'))
  ch=(
    ('Hyderabad','Hyderabad'),

  )
  Name=models.CharField(max_length=255)
  PatientAge=models.IntegerField()
  PatientBloodGroup=models.CharField(choices=CHOICES1,max_length=70)
  Unitsofbloodrequried=models.IntegerField()
  PhoneNumber=models.BigIntegerField()
  Email = models.EmailField(null=True, help_text ='xyz@gmail.com')
  HospitalName=models.CharField(max_length=90)
  Address=models.CharField(max_length=50)
  city=models.CharField(choices=ch,max_length=43,default='1')
  Purpose=models.CharField(max_length=100)