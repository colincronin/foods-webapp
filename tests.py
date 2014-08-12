from django.test import TestCase
from django.core.urlresolvers import reverse

from foods.models import Item

class FoodsTest(TestCase):
    def test_testform(self):
        """
        Test the application's testform view
        """
        response = self.client.get(reverse("foods:testform"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
    def test_item_addition(self):
        """
        Test the behavior of the application's index form submission which should yield a new Item object
        """
        newitem = "Apples"
        response = self.client.post(reverse("foods:testform"),
            {"name": newitem}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, newitem)
    def test_second_item_addition(self):
        """
        Test the behavior of the application's testform upon second form submission
        """
        newitem1 = "Apples"
        newitem2 = "Pears"
        response = self.client.post(reverse("foods:testform"),
            {"name": newitem1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, newitem1)
        response2 = self.client.post(reverse("foods:testform"),
            {"name": newitem2}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response2, newitem1)
        self.assertContains(response2, newitem2)
    def test_item_not_purchased(self):
        """
        Test the display of an unpurchased item
        """
        newitem = "Apples"
        response = self.client.post(reverse("foods:testform"),
            {"name": newitem}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, newitem)
        #self.assertContains(response, "Buy")
        #Check for Buy button which should call a method to save() and set purchased and purchased_date
        #self.assertIn("form", response.context)
        #self.assertIn("object_list", response.context)
        #Check for second form context to add market and price data
