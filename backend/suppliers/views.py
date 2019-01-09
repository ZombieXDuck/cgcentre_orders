from .models import Suppliers, SupplierItems
from .serializers import SupplierSerializer, SupplierItemSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SuppliersView(APIView):
    """
    Return all supplier names and ids
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
            supplierSerializer.save()
            return Response(supplierSerializer.data, status=status.HTTP_201_CREATED)
        return Response(supplierSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierView(APIView):
    """
    Return the name and items of a supplier
    """
    def get(self, request, supplierId, format=None):
        supplier = get_object_or_404(Suppliers, pk=supplierId)
        supplierSerializer = SupplierSerializer(supplier)
        return Response(supplierSerializer.data, status=status.HTTP_200_OK)
        
    """
    Update the name and items of a supplier
    """
    def post(self, request, supplierId, format=None):
        supplier = get_object_or_404(Suppliers, pk=supplierId)
        supplierSerializer = SupplierSerializer(supplier, data=request.data)
        # need to update supplier items
        if supplierSerializer.is_valid():
            supplierSerializer.save()
            return Response(supplierSerializer.data, status=status.HTTP_201_CREATED)
        return Response(supplierSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
