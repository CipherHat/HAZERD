from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.TextField('Company Name')
