from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
import pandas as pd
from scipy.stats import norm
import numpy as np


class Medicine(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    mean_demand = models.FloatField(default=0.0)
    sd_of_demand = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    holding_cost = models.FloatField(default=0.0)
    ordering_cost = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name}'

    def get_total_supplier_lead_time(self):
        cursor = OtherInfo.objects.filter(medicine=self, content_type=ContentType.objects.get_for_model(Supplier))
        sum = 0
        for obj in cursor:
            sum += obj.lead_time
        return sum

    def get_total_centre_lead_time(self):
        cursor = OtherInfo.objects.filter(medicine=self, content_type=ContentType.objects.get_for_model(Centre))
        sum = 0
        for obj in cursor:
            sum += obj.lead_time
        return sum

    def get_total_lead_time(self):
        Sum = self.get_total_centre_lead_time() + self.get_total_supplier_lead_time()
        return Sum

    def get_total_supplier_sd(self):
        cursor = OtherInfo.objects.filter(medicine=self, content_type=ContentType.objects.get_for_model(Supplier))
        sum = 0
        for obj in cursor:
            sum += obj.sd
        return sum

    def get_total_centre_sd(self):
        cursor = OtherInfo.objects.filter(medicine=self, content_type=ContentType.objects.get_for_model(Centre))
        sum = 0
        for obj in cursor:
            sum += obj.sd
        return sum

    def get_total_sd(self):
        sd1 = self.get_total_supplier_sd()
        sd2 = self.get_total_centre_sd()
        sdev = (sd1*sd1 + sd2*sd2)**0.5
        return sdev

    def get_annual_demand(self):
        ls = []
        ls = np.random.normal(self.mean_demand, self.sd_of_demand, 365)
        sum = 0
        for i in ls:
            sum += i
        annual_demand = sum
        return annual_demand

    def get_rop(self):
        ROP = (norm.ppf(0.9, loc=self.mean_demand, scale=self.sd_of_demand) * (((self.get_total_lead_time() * ((self.sd_of_demand) ** 2)) + (((self.mean_demand) ** 2) * ((self.get_total_sd()) ** 2))) ** 0.5)) + self.mean_demand * self.get_total_lead_time()
        return ROP

    def get_OrderFreq(self):
        cursor = Medicine.objects.all()
        b = 0
        c = 0
        for obj in cursor:
            ni = ((obj.holding_cost * obj.price * obj.get_annual_demand()) + (
                        2 * (4000 + obj.ordering_cost))) ** 0.5
            nii = ((obj.holding_cost * obj.price * obj.get_annual_demand()) + (2 * obj.ordering_cost)) ** 0.5
            mi = ni // nii
            num = obj.holding_cost * obj.price * obj.get_annual_demand() * mi
            deno = obj.ordering_cost / mi
            b += num
            c += deno
        c = (c+4000)*2
        n = (b/c)**0.5
        Ord_freq = n // mi
        return Ord_freq

    def get_EOQ(self):
        EOQ = self.get_annual_demand()/self.get_OrderFreq()
        return EOQ

    def get_order_freq_overstock(self):
        f = []
        k = []
        f = np.random.normal(self.mean_demand, self.sd_of_demand, 365)
        x = self.get_EOQ()
        l = 0
        for i in range(len(f)):
            x = x - f[i]
            k.append(x)
            if (x == 0):
                x = self.get_EOQ()
                l += 1
            elif (i!=len(f)-1 and x-f[i+1] < 0):
                x = self.get_EOQ()
                l += 1
        act_order_freq = l
        overstock = k[len(k)-1]
        ans = [act_order_freq, overstock]
        return ans

    def get_act_order_freq(self):
        act_order_freq = self.get_order_freq_overstock()[0]
        return act_order_freq

    def get_overstock(self):
        overstock = self.get_order_freq_overstock()[1]
        return overstock
    

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
