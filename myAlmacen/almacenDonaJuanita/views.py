from django.shortcuts import render
from .models import Detalleboleta,Cliente,Boleta,Producto,Proveedor

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_autent
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
def login (request):
    if request.POST:
        usuario = request.POST.get("txtUsername")
        password = request.POST.get("txtPass")
        usuario = authenticate(request,username=usuario, password=password)
        if usuario is not None and usuario.is_active:
            login_autent(request,usuario)
            return render(request,'web/Index.html')
        else:
            return render(request,'web/login.html', {'msg':'usuario/o contraseña incorrecto'})
    return render(request,'web/login.html')

def index(request):
    return render(request,'web/index.html')

def cliente(request):
    return render(request,'web/cliente.html')

def proveedor(request):
    return render(request,'web/proveedor.html')

@login_required(login_url='/login/')
def guardar_proveedor(request):
        if request.POST:
            idproveedor = request.POST.get("idProveedor")
            telefonoproveedor = request.POST.get("telefonoProveedor")
            correoproveedor = request.POST.get("correoProveedor")


        proveedor = Proveedor(
            idproveedor=idproveedor,
            telefonoproveedor=telefonoproveedor,
            correoproveedor=correoproveedor,
        )

        producto.save()
        return render (request,'web/proveedor.html')

def eliminar_proveedor(request,id):
    try:
        Proveedor = proveedor.objects.get(idproveedor=idproveedor)
        proveedor.delete()
        msg='Elimino Proveedor'
    except:
        msg='No Elimino'
    lista = Producto.objects.all()
    return render(request,'web/proveedor.html',{'listar_proveedor':lista, 'msg':msg})


def venta(request):
    return render(request,'web/venta.html')
@login_required(login_url='/login/')
def guardar_venta(request):
        if request.POST:
            idboleta = request.POST.get("idVenta")
            nombreproducto = request.POST.get("nombreProducto")
            precioventa = request.POST.get("precioProducto")
            stockproducto = request.POST.get("stockProducto")


        venta = venta(
            codigo=idboleta,
            nombreproducto=nombreproducto,
            precioventa=precioventa,
            stock=stockproducto
        )

        Detalleboleta.save()
        return render (request,'web/venta.html')

def eliminar_venta(request,id):
    try:
        producto = Detalleboleta.objects.get(idventa=idventa)
        producto.delete()
        msg='Elimino Producto'
    except:
        msg='No Elimino'
    lista = Producto.objects.all()
    return render(request,'web/venta.html',{'listar_producto':lista, 'msg':msg})

def producto(request):
    return render(request,'web/producto.html')
@login_required(login_url='/login/')
def guardar_producto(request):
        if request.POST:
            idproducto = request.POST.get("idProducto")
            nombreproducto = request.POST.get("nombreProducto")
            precioventa = request.POST.get("precioVenta")
            stockproducto = request.POST.get("stockProducto")

        producto = producto(
            codigo=idproducto,
            nombreproducto=nombreproducto,
            precioventa=precioventa,
            stock=stockproducto
        )

        producto.save()
        return render (request,'web/producto.html')

def eliminar_producto(request,id):
    try:
        producto = Productos.objects.get(idproducto=idproducto)
        producto.delete()
        msg='Elimino Producto'
    except:
        msg='No Elimino'
    lista = Producto.objects.all()
    return render(request,'web/producto.html',{'listar_producto':lista, 'msg':msg})
