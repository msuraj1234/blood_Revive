from django.contrib import admin
from .models import Donor_mdl

@admin.register(Donor_mdl)
class sdata(admin.ModelAdmin):
    list_display = ['donation_id','name','blood_group','age','date_brth','address','phone_no','LastDonateDate']
