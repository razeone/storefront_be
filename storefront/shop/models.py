from django.db import models

# Create your models here.


class Address(models.Model):
    name = models.CharField()
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_number = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
