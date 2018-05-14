from rest_framework import serializers
from .models import Suppliers, SupplierItems

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ('supplierId', 'supplierName')

class SupplierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItems
        fields = ('supplierId', 'supplierItemId', 'itemCode', 'itemName')
