from django.shortcuts import render
from django.contrib import messages
import csv, io
from .models import Medicines, Centres, Suppliers
# Create your views here.

def medicines_upload(request):
    template = "medicines_upload.html"
    prompt = {
        'order' : 'Order of the csv should be Med_name, mean_demand, std._dev_of_demand, Holding_cost, Price, Ordering_cost'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a .csv file')

    data_set = csv_file.read().decode()
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter = ',', quotechar="|"):
        _, created = Medicines.objects.update_or_create(
            med_name = column[0],
            mean_demand = column[1],
            std_dev = column[2],
            Holding_cost = column[3],
            Price = column[4],
            Ordering_cost = column[5]
        )
    context = {}
    return render(request, template, context)