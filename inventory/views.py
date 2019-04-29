from django.views.generic import TemplateView

from inventory.models import Medicine, Supplier, Centre
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class InventoryHome(TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super(InventoryHome, self).get_context_data()

        # add our data
        context['medicine_count'] = Medicine.objects.count()
        context['supplier_count'] = Supplier.objects.count()
        context['centre_count'] = Centre.objects.count()

        return context


class MedicineList(ListView):

    model = Medicine


class MedicineDetails(DetailView):

    model = Medicine

