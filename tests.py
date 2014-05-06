from django.test import TestCase
from django.core.urlresolvers import reverse

from foods.models import Item

# Create your tests here.
class FoodsText(TestCase):
    def test_index(self):
        """
        Test the application's index view
        """
        response = self.client.get(reverse("foods:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
    def test_item_addition(self):
        """
        Test the behavior of the application's index form submission which should yield a new Item object
        """
        newitem = "Apples"
        response = self.client.post(reverse("foods:index"),
            {"name": newitem}, follow=True)
        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, newitem)
