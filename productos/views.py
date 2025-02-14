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
    