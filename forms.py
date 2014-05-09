from django import forms

from foods.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['purchased', 'name', 'price',]
