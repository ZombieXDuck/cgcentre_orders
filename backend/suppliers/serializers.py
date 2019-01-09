from rest_framework import serializers
from .models import Suppliers, SupplierItems

class SupplierItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SupplierItems
        fields = ('item_code', 'item_name')
        
class SupplierSerializer(serializers.ModelSerializer):
    supplier_items = SupplierItemSerializer(many=True)
    
    class Meta:
        model = Suppliers
        fields = ('supplier_name', 'supplier_items')
        
    def create(self, validated_data):
        supplier_items_data = validated_data.pop('supplier_items')
        supplier = Suppliers.objects.create(**validated_data)
        for supplier_item_data in supplier_items_data:
            SupplierItems.objects.create(supplier=supplier, **supplier_item_data)
        return supplier
