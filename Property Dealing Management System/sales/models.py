from django.db import models

# Create your models here.
class PropertyForRent(models.Model):
    p_no = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    rooms = models.CharField(max_length=20)
    rent = models.CharField(max_length=20)
    owner_no = models.CharField(max_length=20)
