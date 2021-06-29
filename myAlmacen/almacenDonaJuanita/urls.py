from django.contrib import admin
from django.urls import path,include
from .views import login,index,cliente, producto,proveedor,venta,modproducto,modproveedor,base,listar_clientes,eliminar_cliente

urlpatterns = [
    path('',login,name='LOGIN'),
    path('index.html',index,name='INDEX'),
    path('cliente.html',cliente,name='CLIENTE'),
    path('proveedor.html',proveedor,name='PROVEEDOR'),
    path('modproveedor.html',modproveedor,name='MODPROVEEDOR'),
    path('venta.html',venta,name='VENTA'),
    path('producto.html',producto,name='PRODUCTO'),
    path('modproducto.html',modproducto,name='MODPRODUCTO'),
    path('base.html',base,name='base'),
    path('listarclientes.html',listar_clientes,name='LISCLIENTES'),
    path('eliminarCliente/<idcliente>/',eliminar_cliente,name='ELIMINARCLIENTE'),

]