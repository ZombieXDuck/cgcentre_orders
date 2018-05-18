from .models import Suppliers, SupplierItems
from .serializers import SupplierSerializer, SupplierItemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SupplierList(APIView):
    """
    List all suppliers, or create a supplier.
    """
    def get(self, request, format=None):
        suppliers = Suppliers.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

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
    List all supplier items, or create supplier items.
    """
    def get(self, request, supplierId, format=None):
        supplierItems = SupplierItems.objects.filter(supplierId = supplierId)
        serializer = SupplierItemSerializer(supplierItems, many=True)
        return Response(serializer.data)
    """
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
