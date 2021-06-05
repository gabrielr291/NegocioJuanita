from django.contrib import admin
from django.urls import path,include
from .views import login,index,cliente, producto,proveedor,venta

urlpatterns = [
    path('',login,name='LOGIN'),
    path('index.html',index,name='INDEX'),
    path('cliente.html',cliente,name='CLIENTE'),
    path('proveedor.html',proveedor,name='PROVEEDOR'),
    path('venta.html',venta,name='VENTA'),
    path('producto.html',producto,name='PRODUCTO'),

]