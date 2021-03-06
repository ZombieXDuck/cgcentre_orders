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
        fields = ('id', 'supplier_name', 'supplier_items')
        
    def create(self, validated_data):
        supplier_items_data = validated_data.pop('supplier_items')
        supplier = Suppliers.objects.create(**validated_data)
        for supplier_item_data in supplier_items_data:
            SupplierItems.objects.create(supplier=supplier, **supplier_item_data)
        return supplier

    def update(self, instance, validated_data):
        instance.supplier_name = validated_data.get('supplier_name', instance.supplier_name)
        supplier_items_data = validated_data.pop('supplier_items')
        for supplier_item_data in supplier_items_data:
            supplier_item = SupplierItems.objects.get(pk=supplier_item_data)
            supplier_item.item_code = supplier_item_data.item_code
            supplier_item.item_name = supplier_item_data.item_name
        instance.save()
        return instance