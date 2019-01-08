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
        
    def create(self, validated_data):
        supplier_items_data = validated_data.pop('supplierItems')
        supplier = Supplier.objects.create(**validated_data)
        for supplier_item_data in supplier_items_data:
            SupplierItems.objects.create(supplier=supplier, **supplier_item_data)
        return supplier
