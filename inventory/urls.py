from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.InventoryHome.as_view(), name='index'),
    path('medicine/', views.MedicineList.as_view(), name='medicine_list'),
    path('medicine/<int:pk>/', views.MedicineDetails.as_view(), name='medicine_detail')
]
