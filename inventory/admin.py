from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Medicine)
admin.site.register(Centre)
admin.site.register(Supplier)
admin.site.register(OtherInfo)
