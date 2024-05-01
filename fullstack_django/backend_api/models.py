from django.db import models

# # Create your models here.

class Chair(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    # material = models.CharField(max_length=50)
    # color = models.CharField(max_length=50)
    # box_size = models.CharField(max_length=50, blank=True, null=True)
    # product_size = models.CharField(max_length=50, blank=True, null=True)
    # without_box_size = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    # shape = models.CharField(max_length=50)
    # material = models.CharField(max_length=50)
    # box_size = models.CharField(max_length=50, blank=True, null=True)
    # product_size = models.CharField(max_length=50, blank=True, null=True)
    # without_box_size = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
