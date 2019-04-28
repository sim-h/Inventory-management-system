from django.contrib import admin

from .models import *


# Register your models here.


class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'mean', 'sd', 'price', 'holding_cost', 'ordering_cost']


admin.site.register(Medicine, MedicineAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Supplier, SupplierAdmin)


class CentreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Centre, CentreAdmin)


class OtherInfoAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'medicine', 'lead_time', 'sd']
    list_filter = ['content_type']


admin.site.register(OtherInfo, OtherInfoAdmin)
