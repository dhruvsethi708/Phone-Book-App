from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=12, blank=False, unique=True)