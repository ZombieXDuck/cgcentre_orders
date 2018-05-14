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
    """
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

class SupplierItemList(APIView):
    """
    List all supplier items, or create supplier items.
    """
    def get(self, request, format=None):
        supplierItems = SupplierItems.objects.all()
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
