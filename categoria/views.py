from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from  .forms import CategoriaForm

# Create your views here.

# Vista que muestra el formulario para agregar un producto
def agregar_categoria(request):
    #Checar si vengo del formulario
    if request.method == 'POST':
        #Quiere decir que enviarion el formulario
        form = CategoriaForm(request.POST)
        #Checar si el formulario es valido
        if form.is_valid():
            #Guardar el producto en la base de datos
            form.save()
            return redirect('ver')
    #Si no se envió el formulario o no es válido
    else:
        form = CategoriaForm()
    return render(request, 'agregarCategoria.html', {'form': form})


# Vista que devuelve los productos como JSON
def lista_categoria(request):
    #Obtener todos los objetos productos de la base de datos
    categoria = Categoria.objects.all()

    # Guardar los datos en un diccionario
    # Este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categoria
    ]

    return JsonResponse(data, safe=False)

# Vistas que devuelven los productos como JSON
def ver_categorias(request):
    return render(request, 'verCategoria.html')

import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Categoria

# Función que permite registrar una categoría como objeto JSON
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Categoría registrada correctamente',
                'id': categoria.id
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no soportado'}, status=405)

# Función para actualizar una categoría
def actualizar_categoria(request, id_categoria):
    if request.method == 'PUT':
        categoria = get_object_or_404(Categoria, id=id_categoria)
        try:
            data = json.loads(request.body)
            categoria.nombre = data.get('nombre', categoria.nombre)
            categoria.imagen = data.get('imagen', categoria.imagen)
            categoria.save()
            return JsonResponse({'mensaje': 'Categoría actualizada correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no soportado'}, status=405)

# Función para borrar una categoría
def borrar_categoria(request, id_categoria):
    if request.method == 'DELETE':
        categoria = get_object_or_404(Categoria, id=id_categoria)
        categoria.delete()
        return JsonResponse({'mensaje': 'Categoría eliminada correctamente'}, status=200)
    return JsonResponse({'error': 'Método no soportado'}, status=405)

# Función para obtener una categoría específica
def obtener_categoria(request, id_categoria):
    if request.method == 'GET':
        categoria = get_object_or_404(Categoria, id=id_categoria)
        data = {
            'id': categoria.id,
            'nombre': categoria.nombre,
            'imagen': categoria.imagen,
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'error': 'Método no soportado'}, status=405)