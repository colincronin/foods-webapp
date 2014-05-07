from django.shortcuts import render
from django.views.generic.edit import CreateView

from foods.models import Item

class ItemAdd(CreateView):
    model = Item
    fields = ["name"]

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Item.objects.order_by('id')
        return super(ItemAdd, self).get_context_data(**kwargs)
