from django.contrib import admin
from .models import Blood_donor_model

# Register your models here.
@admin.register(Blood_donor_model)
class receiverAdmin(admin.ModelAdmin):
    list_display = ['Name','PatientBloodGroup','PhoneNumber','Email','city','Purpose']