from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    mean = models.FloatField(default=0.0)
    sd = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    holding_cost = models.FloatField(default=0.0)
    ordering_cost = models.FloatField(default=0.0)
    Supplier_name = models.CharField(max_length=100)
    Centre_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


# class Centre(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class Supplier(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.name}'


class OtherInfo(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    sd = models.FloatField(default=0.0)
    lead_time = models.FloatField(default=0.0)

    limit = models.Q(app_label='inventory', model='centre') | models.Q(app_label='inventory', model='supplier')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.medicine.name}'
