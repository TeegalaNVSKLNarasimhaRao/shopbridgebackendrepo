from .test_setup import TestSetup
from django.urls import reverse
import json

class TestViews(TestSetup):

    def test_inventory_cannot_created(self):
        res = self.client.post(self.inventory_list_url)
        self.assertEqual(res.status_code, 400)
    
    def test_inventory_can_created(self):
        res = self.client.post(self.inventory_list_url, self.inventory_data, format="json")
        json_res = json.loads(res.content)
        self.assertEqual(json_res['name'], self.inventory_data['name'])
        self.assertEqual(json_res['description'], self.inventory_data['description'])
        self.assertEqual(res.status_code, 201)
    
    def test_inventory_get_updated(self):
        res = self.client.post(self.inventory_list_url, self.inventory_data, format="json")
        res_updated = self.client.put(reverse("inventory_detail", kwargs={"pk": json.loads(res.content)["id"]}), self.inventory_updated_data, format="json")
        json_res = json.loads(res_updated.content)
        self.assertEqual(json_res['name'], self.inventory_updated_data['name'])
        self.assertEqual(json_res['description'], self.inventory_updated_data['description'])
        self.assertEqual(res_updated.status_code, 200)

    def test_inventory_get_reviwed(self):
        res = self.client.post(self.inventory_list_url, self.inventory_data, format="json")
        res_get = self.client.get(reverse("inventory_detail", kwargs={"pk": json.loads(res.content)["id"]}))
        json_res = json.loads(res_get.content)
        self.assertEqual(json_res['name'], self.inventory_data['name'])
        self.assertEqual(json_res['description'], self.inventory_data['description'])
        self.assertEqual(res_get.status_code, 200)

    def test_inventory_get_destroyed(self):
        res = self.client.post(self.inventory_list_url, self.inventory_data, format="json")
        res_get = self.client.delete(reverse("inventory_detail", kwargs={"pk": json.loads(res.content)["id"]}))
        res_inventory_all = self.client.get(self.inventory_list_url)
        json_res = json.loads(res_inventory_all.content)
        self.assertEqual(len(json_res), 0)
        self.assertEqual(res_get.status_code, 204)