from .models import Suppliers, SupplierItems
from .serializers import SupplierSerializer, SupplierItemSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SupplierList(APIView):
    """
    Return all suppliers
    """
    def get(self, request, format=None):
        suppliers = Suppliers.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)
    """
    Create a supplier along with initial items
    """
    def post(self, request, format=None):
        supplierSerializer = SupplierSerializer(data=request.data)
        if supplierSerializer.is_valid():
            supplier = supplierSerializer.save()
            for item in request.data['supplierItems']: item['supplierId'] = supplier.supplierId
            supplierItemSerializer = SupplierItemSerializer(data=request.data['supplierItems'], many=True)
            if supplierItemSerializer.is_valid():
                supplierItemSerializer.save()
                return Response(supplierSerializer.data, status=status.HTTP_201_CREATED)
            return Response(supplierItemSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(supplierSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierItemList(APIView):
    """
    Return the name and items of a supplierId
    """
    def get(self, request, supplierId, format=None):
        #get supplier
        supplier = get_object_or_404(Suppliers, pk=supplierId)
        supplierSerializer = SupplierSerializer(supplier)
        #get supplier items
        supplierItems = SupplierItems.objects.filter(supplierId=supplierId)
        supplierItemSerializer = SupplierItemSerializer(supplierItems, many=True)
        #return suplier name and supplier items
        return Response({
            'supplierName': supplierSerializer.data['supplierName'],
            'supplierItems': supplierItemSerializer.data,
        })
    """
    Add supplier items to a list belonging to a supplierId
    """
    """
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
