from django.db import models

# Create your models here.


class suggestion(models.Model):
    name1 = models.CharField(max_length=10, default=None)
    email = models.EmailField(default=None)
    others = models.TextField(max_length=100)
