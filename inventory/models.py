from django.db import models

# Create your models here.


class Medicines(models.Model):

    med_name = models.CharField(max_length=100)
    mean_demand = models.FloatField(default=0)
    std_dev = models.FloatField(default=0)
    Holding_cost = models.FloatField(default=0)
    Price = models.FloatField(default=0)
    Ordering_cost = models.FloatField(default=0)

    def __str__(self):
        return f'{self.med_name}'

class Centres(models.Model):
    Centre_name = models.CharField(max_length=100)
    med_name = models.CharField(max_length=100)
    Lead_time = models.FloatField(default=0)
    Std_dev = models.FloatField(default=0)

    def __str__(self):
        return f'{self.Centre_name}'

class Suppliers(models.Model):
    Supp_name = models.CharField(max_length=100)
    med_name = models.CharField(max_length=100)
    LT = models.FloatField(default=0)
    Sdev = models.FloatField(default=0)

    def __str__(self):
        return f'{self.Supp_name}'