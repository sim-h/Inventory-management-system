from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *


# Register your models here.


class OtherInfoAdmin(GenericTabularInline):
    model = OtherInfo


class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'mean_demand', 'sd_of_demand', 'price', 'holding_cost', 'ordering_cost']
    list_editable = ['mean_demand', 'sd_of_demand', 'price', 'holding_cost', 'ordering_cost']


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'medicine_count']
    inlines = [OtherInfoAdmin]

    @staticmethod
    def medicine_count(obj):
        return OtherInfo.objects.filter(object_id=obj.id, content_type__model='supplier').count()


class CentreAdmin(admin.ModelAdmin):
    list_display = ['name', 'medicine_count']
    inlines = [OtherInfoAdmin]

    @staticmethod
    def medicine_count(obj):
        return OtherInfo.objects.filter(object_id=obj.id, content_type__model='centre').count()


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Centre, CentreAdmin)
