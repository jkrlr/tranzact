from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=40)
    company_email = models.EmailField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.company_name)