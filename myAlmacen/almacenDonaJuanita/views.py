from django.shortcuts import render
from .models import Detalleboleta,Cliente,Boleta,Producto,Proveedor,Usuario,Estadopedido,Familiaproducto,Pedido,Rubroproveedor,Tipoproducto
from django.http import HttpResponse

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

def modproveedor(request):
    return render(request,'web/modproveedor.html')

def agregar_proveedor(request):
        if request.POST:
            telefono = request.POST.get("phone")
            correo = request.POST.get("email")
            nombre = request.POST.get("txtname")

            if nombre==True:
                proveedordatos = Proveedor()
                proveedordatos.telefonoproveedor = telefono
                proveedordatos.correoproveedor = correo
                proveedordatos.nombreproveedor = nombre

                Proveedor.save()
            return render({'msg':'Proveedor guardado'})
        return render (request,'web/proveedor.html')

def eliminar_proveedor(request):

    return render(request,'web/proveedor.html',{})


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
def modproducto(request):
    return render(request,'web/modproducto.html')
@login_required(login_url='/login/')
def guardar_producto(request):
        if request.POST:
            nombre = request.POST.get("txtname")
            desc = request.POST.get("txtdescuento")
            fechaven = request.POST.get("fechavenci")
            pcompra = request.POST.get("preciocompra")
            pventa = request.POST.get("precioventa")
            stock = request.POST.get("stock")
            critico = request.POST.get("stockcritico")

            if nombre==True:
                productosdatos = Producto()
                productosdatos.nombreproducto = nombre
                productosdatos.descproducto = desc
                productosdatos.fechavencimiento = fechaven
                productosdatos.preciocompra = pcompra
                productosdatos.precioventa = pventa
                productosdatos.stockproducto = stock
                productosdatos.stockcriticoproducto = critico
                

                Producto.save()
            return render({'msg':'Producto guardado'})
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





def agregar_detalleboleta(request):
    carro = Detalleboleta(request.session)
    producto = Producto.objects.get(idproducto=request.GET.get('idproducto'))
    carro.add(producto, precio=producto.precioventa)
    return HttpResponse("AGREGADO")


def eliminar_productocarro(request):
    carro = Detalleboleta(request.session)
    producto = Producto.objects.get(idproducto=request.GET.get('idproducto'))
    carro.remove(producto)
    return HttpResponse("ELIMINADO")


def mostrar_productocarro(request):
    return render(request, 'web/mostrar-carro.html')
