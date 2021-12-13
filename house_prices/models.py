from django.db import models

# Create your models here.
from django.db import models


class Transaction(models.Model):
    uid = models.CharField(max_length=50, primary_key=True)
    price = models.IntegerField()
    date = models.DateTimeField()
    postcode = models.CharField(max_length=10)
    property_type = models.CharField(max_length=1, choices=[('D', 'Detached'), ('S', 'Semi-Detached'), ('T', 'Terraced'), ('F', 'Flat'), ('O', 'Other')])
    new = models.BooleanField()
    duration = models.CharField(max_length=1, choices=[('F', 'Freehold'), ('L', 'Leasehold')])
    poan = models.CharField(max_length=100)
    soan = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    standard = models.CharField(max_length=1, choices=[('A', 'Standard'), ('B', 'Repo')])
    record = models.CharField(max_length=1, choices=[('A', 'Add'), ('D', 'Delete'), ('C', 'Change')], default='A')
