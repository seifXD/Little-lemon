from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu_item1 = Menu.objects.create(title="Pizza Margherita", price=8.99, inventory=10)
        self.menu_item2 = Menu.objects.create(title="Caesar Salad", price=6.99, inventory=15)
        self.menu_item3 = Menu.objects.create(title="Spaghetti Carbonara", price=10.99, inventory=20)
