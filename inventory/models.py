from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    mean = models.FloatField(default=0.0)
    sd = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    holding_cost = models.FloatField(default=0.0)
    ordering_cost = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name}'


class Centre(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Supplier(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return f'{self.name}'


class OtherInfo(models.Model):
    MODEL_CHOICES = models.Q(app_label='inventory', model='centre') | models.Q(app_label='inventory', model='supplier')

    # center or supplier
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=MODEL_CHOICES)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # params
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, db_index=True)
    lead_time = models.FloatField(default=0.0)
    sd = models.FloatField(default=0.0)

    class Meta:
        index_together = [
            ["content_type", "object_id"],
        ]
        unique_together = ["content_type", "object_id", "medicine"]

    def __str__(self):
        return f'{self.medicine.name}'
