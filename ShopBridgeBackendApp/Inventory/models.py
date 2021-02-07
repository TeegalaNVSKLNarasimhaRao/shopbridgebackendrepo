from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    price = models.DecimalField(blank=False, decimal_places=4, max_digits=8)
