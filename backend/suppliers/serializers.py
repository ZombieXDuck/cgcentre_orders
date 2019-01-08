from rest_framework import serializers
from .models import Suppliers, SupplierItems

class SupplierItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SupplierItems
        fields = ('supplierId', 'supplierItemId', 'itemCode', 'itemName')
        
class SupplierSerializer(serializers.ModelSerializer):
    supplierItems = SupplierItemSerializer(many=True)
    
    class Meta:
        model = Suppliers
        fields = ('supplierId', 'supplierName', 'supplierItems')
