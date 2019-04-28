from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.InventoryHome.as_view(), name='index'),
]
