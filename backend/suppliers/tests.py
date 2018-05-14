from rest_framework import status
from suppliers.models import Suppliers, SupplierItems
from django.test import TestCase, Client

class SupplierTestViews(TestCase):
    def setUp(self):
        supplier = Suppliers.objects.create(supplierName='Richgro')
        SupplierItems.objects.create(supplierId=supplier, itemCode=3452, itemName='small plant')
        self.client = Client()

    def test_get_suppliers(self):
        response = self.client.get('/suppliers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        supplier = Suppliers.objects.get(supplierId = 1)
        self.assertEqual(supplier.supplierName, 'Richgro')

    def test_get_supplier_items(self):
        response = self.client.get('/suppliers/', {'supplierId': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        supplierItems = SupplierItems.objects.get(supplierItemId = 1)
        self.assertEqual(supplierItems.itemName, 'small plant')
        self.assertEqual(supplierItems.itemCode, '3452')

    #def test_post(self):
    #    response = self.client.post('/suppliers/', {'name': 'ben', 'email': 'ben@gmail.com'}, follow=True)
    #    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #    self.assertEqual(Person.objects.count(), 3)
    #    self.assertEqual(Person.objects.get(name='ben').name, 'ben')
