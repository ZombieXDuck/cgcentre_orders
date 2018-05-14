from django.db import models

class Orders(models.Model):
    orderId = models.AutoField(primary_key = True)
    supplierId = models.ForeignKey('suppliers.Suppliers', on_delete = models.CASCADE)
    ordered = models.BooleanField(default = False)

class OrderItems(models.Model):
    orderItemId = models.AutoField(primary_key = True)
    orderId = models.ForeignKey('Orders', on_delete = models.CASCADE)
    supplierItemId = models.ForeignKey('suppliers.SupplierItems', on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
