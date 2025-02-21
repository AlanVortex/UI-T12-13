from django.shortcuts import render, redirect
#render: pinta una plantilla
#redirect: redirecciona a una URL
from .models import Producto
#Este objeto me permite enviar respuestas JSON
from django.http import JsonResponse
from .forms import productoForm

#Vista que maneja y carga el formulario
def agregar_producto(request):
    if request.method == 'POST':
        #Crear un objeto de tipo formulario
        form = productoForm(request.POST)
        
        #Validar los datos del formulario
        if form.is_valid(): 
            #Guardar los datos en la base de datos
            form.save()
            
            #Redireccionar a una URL
            return redirect('ver')
        
    #Si no es un método POST se crea un formulario vacío
    else:
        #Crear un objeto de tipo formulario
        form = productoForm()
    return render (request, 'agregar.html', {'form': form})



def lista_productos(request):
    #Obtener todos los productos de la base de datos
    productos = Producto.objects.all()
     
    #Guardar los datos en un diccionario
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request, 'ver.html')

import json
#funcion que permite registrar un producto como objeto json    
def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto = Producto.objects.create( #create mete directamente el objeto en la base de datos
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Producto registrado correctamente',
                'id': producto.id
                } , status=201)
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error': str(e)}, status=400)
    return JsonResponse(
        {
            'error': 'Método no soportado', 
        }, status=405
    )

from django.shortcuts import get_object_or_404
#funciones para el metodo put
def actualizar_producto(request, id_producto):
    if request.method == 'PUT':
        producto = get_object_or_404(Producto, id=id_producto)
        try:
            #la informacion de la modificacion del producto viene del body del request
            data = json.loads(request.body)
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            producto.save()
            return JsonResponse({
                'mensaje': 'Producto actualizado correctamente'
            }, status=200)
        except Exception as e:
            return JsonResponse(
                {'error': str(e)}, status=400)
    return JsonResponse(
        {
            'error': 'Método no soportado', 
        }, status=405
    )

#funciones para delete
def borrar_producto(request, id_producto):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete()
        return JsonResponse({
            'mensaje': 'Producto eliminado correctamente'
        }, status=200)
    return JsonResponse(
        {
            'error': 'Método no soportado', 
        }, status=405
    )

#funcion adicional para get con el objetivo de 
# retornar un producto en especifico
def obtener_producto(request, id_producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id_producto)
        data = {
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen,
        }
        return JsonResponse(data, status=200)
    return JsonResponse(
        {
            'error': 'Método no soportado', 
        }, status=405
    )