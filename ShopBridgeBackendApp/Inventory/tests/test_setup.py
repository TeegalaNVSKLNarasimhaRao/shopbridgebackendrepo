from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetup(APITestCase):
    
    def setUp(self) -> None:
        self.inventory_list_url = reverse("inventorys")
        
        self.inventory_data = {
            "name": "product",
            "description": "item is created",
            "price": 20.321
        }

        self.inventory_updated_data = {
            "name": "product updated",
            "description": "item is updated",
            "price": 50.621
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()