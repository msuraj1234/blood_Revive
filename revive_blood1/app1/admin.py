from django.contrib import admin
from .models import suggestion

# Register your models here.
@admin.register(suggestion)
class suggestAdmin(admin.ModelAdmin):
    list_display = ['name1','others']
