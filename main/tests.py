from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def create_item(self):
        self.item = Product.objects.create(
            name        = "Nasi Putih",
            amount      = 1,
            description = "Nasi putih pulen",
        )
        return self.item
    
    def test_create_item(self):
        i = self.create_item()
        self.assertTrue(isinstance(i, Product))