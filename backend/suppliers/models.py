from django.db import models

class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=255)

class SupplierItems(models.Model):
    supplier = models.ForeignKey('Suppliers', related_name='supplier_items', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
