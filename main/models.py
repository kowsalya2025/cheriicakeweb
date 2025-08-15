from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50)  # Must match a URL pattern name
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Sweet(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='sweets/')
    description = models.TextField()
    weight_options = models.CharField(max_length=200, blank=True)  # "500g, 1kg, 2kg"



    def __str__(self):
        return self.name

