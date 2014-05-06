from django.db import models
from django.core.urlresolvers import reverse

class Item(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('foods:index')
