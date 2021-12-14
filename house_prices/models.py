from django.db import models

# Create your models here.
from django.db import models
from dbview.models import DbView


class CsvData(models.Model):
    uid = models.CharField(max_length=50, primary_key=True)
    price = models.IntegerField()
    date = models.DateTimeField()
    postcode = models.CharField(max_length=10, blank=True, null=True)
    property_type = models.CharField(max_length=1,
                                     choices=[('D', 'Detached'), ('S', 'Semi-Detached'), ('T', 'Terraced'),
                                              ('F', 'Flat'), ('O', 'Other')])
    new = models.BooleanField()
    duration = models.CharField(max_length=1, choices=[('F', 'Freehold'), ('L', 'Leasehold')])
    poan = models.CharField(max_length=100, blank=True, null=True)
    soan = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    locality = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    standard = models.CharField(max_length=1, choices=[('A', 'Standard'), ('B', 'Repo')])
    record = models.CharField(max_length=1, choices=[('A', 'Add'), ('D', 'Delete'), ('C', 'Change')], default='A')


class Postcode(models.Model):
    uid = models.AutoField(primary_key=True, auto_created=True, default=1)
    area = models.CharField(max_length=2)
    district = models.CharField(max_length=2)
    sector = models.IntegerField()
    unit = models.CharField(max_length=2)

    def _print_me(self):
        "Postcode(area={},district={},sector={},unit={})".format(self.area,
                                                                 self.district,
                                                                 self.sector,
                                                                 self.unit)

    def __repr__(self):
        return self._print_me()

    def __str__(self):
        return self._print_me()


class Address(models.Model):
    uid = models.AutoField(primary_key=True, auto_created=True, default=1)
    postcode = models.ForeignKey(Postcode, on_delete=models.CASCADE, blank=True, null=True)
    poan = models.CharField(max_length=100, blank=True, null=True)
    soan = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    locality = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)


class Transaction(models.Model):
    uid = models.CharField(max_length=50, primary_key=True)
    price = models.IntegerField()
    date = models.DateTimeField()
    property_type = models.CharField(max_length=1,
                                     choices=[('D', 'Detached'), ('S', 'Semi-Detached'), ('T', 'Terraced'),
                                              ('F', 'Flat'), ('O', 'Other')])
    new = models.BooleanField()
    duration = models.CharField(max_length=1, choices=[('F', 'Freehold'), ('L', 'Leasehold')])
    standard = models.CharField(max_length=1, choices=[('A', 'Standard'), ('B', 'Repo')])
    record = models.CharField(max_length=1, choices=[('A', 'Add'), ('D', 'Delete'), ('C', 'Change')], default='A')
    Address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None)


class UniquePostcodes(DbView):
    postcode = models.CharField(primary_key=True, max_length=10, blank=True)

    @classmethod
    def view(cls):
        qs = CsvData.objects.values('postcode').distinct()
        return str(qs.query)
