from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Menu
import json
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu_item1 = Menu.objects.create(title="Pizza Margherita", price=8.99, inventory=10)
        self.menu_item2 = Menu.objects.create(title="Caesar Salad", price=6.99, inventory=15)
        self.menu_item3 = Menu.objects.create(title="Spaghetti Carbonara", price=10.99, inventory=20)

    def test_getall(self):
        url = reverse('MenuItemsView') # takes a view name as an argument and returns the corresponding URL
        response = self.client.get(url) # sends a GET request to the URL returned by 'reverse' and stores the response in the 'response' variable
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu_items = Menu.objects.all() # gets a queryset of all 'Menu' objects from the database
        serializer = MenuSerializer(menu_items, many = True) # serializes the queryset of 'Menu' objects into a JSON-like format
        self.assertEqual(response.data, serializer.data)
        