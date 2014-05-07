from django.db import models
from django.core.urlresolvers import reverse

class Item(models.Model):
    name = models.CharField(max_length=50)
    purchased = models.BooleanField(default=False)
    purchased_date = models.DateField(null=True, blank=True)
    market = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.id,self.name)
    def get_absolute_url(self):
        return reverse('foods:index')
    def was_purchased(self):
        if self.purchased:
            return True
        elif not self.purchased:
            return False
