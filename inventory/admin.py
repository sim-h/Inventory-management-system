from django.contrib import admin

# Register your models here.

from .models import Medicines, Centres, Suppliers

admin.site.register(Medicines)
admin.site.register(Centres)
admin.site.register(Suppliers)
