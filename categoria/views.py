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