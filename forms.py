from django import forms

from foods.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['purchased', 'name', 'price',]
        labels = {
            'price': ('$'),
        }
        widgets = {
            'price': forms.TextInput(attrs={
                'type': 'number',
                'size': '6',
                'step': '0.01',
                'decimal_places': '2',
             }),
        }
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['purchased'].widget.attrs['onClick'] = "this.form.submit();"
        self.fields['price'].widget.attrs['onBlur'] = "myFunction(this.id, this.value)"
        self.fields['price'].widget.attrs['onKeyPress'] = "enterFunction(event, this.id, this.value)"
