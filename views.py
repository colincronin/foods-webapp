from django.shortcuts import render
from django.views.generic.edit import CreateView

from foods.models import Item

class ItemAdd(CreateView):
    model = Item
    fields = ["name"]
