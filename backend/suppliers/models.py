from django.db import models

class Suppliers(models.Model):
    supplierId = models.AutoField(primary_key = True)
    supplierName = models.CharField(max_length=255)

class SupplierItems(models.Model):
    supplierItemId = models.AutoField(primary_key = True)
    supplierId = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    itemCode = models.CharField(max_length=255)
    itemName = models.CharField(max_length=255)
