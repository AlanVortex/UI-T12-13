from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from app.utils import google_search

from app.models import Usuarios

from django.http import JsonResponse

from app.models import ErrorLog

# def index(request):
#     return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def index(request):
    return render(request, 'index.html', status=200)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def generar_error(request):
    return 7/0 

def onepage (request):
    return render(request, 'onepage.html', status=200)

def prueba_front (request):
    texto = request.GET.get('texto','')
    #vamos a generar información en python
    objeto1 = {
        'id':'001',
        'titulo': texto,
        'descripcion': 'descripcion de objeto 1'
    }
    objeto2 = {
        'id':'002',
        'titulo': 'titulo de objeto 2',
        'descripcion': 'descripcion de objeto 2'
    }
    objeto3 = {
        'id':'003',
        'titulo': 'titulo de objeto 3',
        'descripcion': 'descripcion de objeto 3'
    }

    conjunto = [objeto1, objeto2, objeto3]

    #Obtener los datos de la base de datos
    personas = Usuarios.objects.values('id', 'nombres', 'apellidos', 'edad')
    listPersonas = list(personas)

    #Como mandar un objeto variable de python a la vista
    return render(
        request,
        'prueba.html',
        {'objeto1': objeto1, 'arreglo': conjunto, 'list': listPersonas},
)

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})