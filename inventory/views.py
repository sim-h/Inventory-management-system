from django.views.generic import TemplateView

from inventory.models import Medicine, Supplier, Centre


class InventoryHome(TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super(InventoryHome, self).get_context_data()

        # add our data
        context['medicine_count'] = Medicine.objects.count()
        context['supplier_count'] = Supplier.objects.count()
        context['centre_count'] = Centre.objects.count()

        return context
