from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView
from django.forms.models import modelformset_factory
from django.template import RequestContext

from foods.models import Item
from foods.forms import ItemForm

class ItemAdd(CreateView):
    model = Item
    fields = ["name"]

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Item.objects.order_by('id')
        return super(ItemAdd, self).get_context_data(**kwargs)

def testform(request):
    ItemFormSet = modelformset_factory(Item, form=ItemForm, can_delete=True)
    if request.method == 'POST':
        formset = ItemFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = ItemFormSet()
    return render_to_response("foods/testform.html",
        {'formset':formset},
        context_instance=RequestContext(request),
    )
