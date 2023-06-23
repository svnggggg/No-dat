import datetime
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.db.models import Q
from proa.models import Alumno, Curso, Calificaciones,Profesor,Materia
from django.db import connection
from django.shortcuts import get_object_or_404
from datetime import datetime


TEMPLATE_DIR = ('os.path.join(BASE_DIR,"templates")')


def index(request):
    calificaciones = Calificaciones.objects.all()
    profesores = Profesor.objects.all()
    cursos = Curso.objects.all()
    materias=Materia.objects.all()
    alumnos=Alumno.objects.all()
    return render(request, 'calificaciones/index.html',{ "calificaciones": calificaciones,"materias": materias, "cursos": cursos, "profesores": profesores, "alumnos":alumnos})

def parse_fecha(fecha_str):
    meses = {
        'enero': '01',
        'febrero': '02',
        'marzo': '03',
        'abril': '04',
        'mayo': '05',
        'junio': '06',
        'julio': '07',
        'agosto': '08',
        'septiembre': '09',
        'octubre': '10',
        'noviembre': '11',
        'diciembre': '12'
    }
    
    partes = fecha_str.split(' ')
    dia = partes[0]
    mes = meses[partes[2]]
    anio = partes[4]
    
    return f"{anio}-{mes}-{dia}"

def guardar_calificaciones(request):
    alumno=request.POST["alumno"]
    curso = request.POST["curso"]
    materia=request.POST["materia"]
    profesor=request.POST["profesor"]
    fecha = request.POST["fecha"]
    fecha_nota_str = datetime.strptime(fecha, "%m/%d/%Y").strftime("%Y-%m-%d")
    nota = request.POST["nota"]
    final = request.POST.get("final") == "on"  # Conversión a True si está marcado
    
    insert = Calificaciones(
        alumno=Alumno.objects.get(dni=alumno),
        curso=Curso.objects.get(id=curso),
        materia=Materia.objects.get(id=materia),
        profesor=Profesor.objects.get(dni=profesor),
        fecha=fecha_nota_str,
        nota=nota,
        final=final,
        )
    insert.save()
    calificaciones = Calificaciones.objects.all()
    return render(request, 'calificaciones/index.html', {"mensaje": "Se insertó calificación con éxito", "calificaciones": calificaciones})


def eliminar_calificaciones(request):
    DNI = request.GET["DNI"]
    delete = get_object_or_404(Calificaciones, dni=DNI)
    delete.delete()
    calificaciones = Calificaciones.objects.all()
    return render(request, 'calificaciones/index.html',{ "mensaje": "Se elimino la calificacion con exito", "calificaciones": calificaciones})

def editar_calificaciones(request):
    DNI = request.GET["DNI"]
    calificaciones = Calificaciones.objects.all()
    calificaciones_editar = Calificaciones.objects.get(dni=DNI)
    print("editar", calificaciones_editar.nombre)
    return render(request, 'calificaciones/index.html', {"mensaje": "", "alumnos": calificaciones, "alumnos_edit": calificaciones_editar})

def guardar_edit(request):
    
    DNI = request.POST["DNI"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    email = request.POST["email"]
    fecha_nacimiento_str = request.POST["fecha_nacimiento"]
    fecha_nacimiento = parse_fecha(fecha_nacimiento_str)
    repitio = request.POST.get("repitio") 
    curso = request.POST["curso"]

    calificaciones = Calificaciones.objects.all()
    Alumno.objects.filter(dni = DNI).update(nombre=nombre, apellido=apellido, email=email, dni=DNI, curso=Curso.objects.get(id=curso), fecha_nacimiento=fecha_nacimiento, repitio=repitio)
    return render(request, 'calificaciones/index.html', {"mensaje": "se editó correctamente", "calificaciones": calificaciones})


def curso(request):
    año = request.GET["curso"]
    print (año)
    if año == "1":
        alumnos = Alumno.objects.filter(curso=año)
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})
    elif año == "2":
        alumnos = Alumno.objects.filter(curso=año)
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})
    elif año == "3":
        alumnos = Alumno.objects.filter(curso = año)
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})
    elif año == "4":
        alumnos = Alumno.objects.filter(curso = año)
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})
    elif año == "5":
        alumnos = Alumno.objects.filter(curso = año)
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})
    elif año == "6":
        alumnos = Alumno.objects.filter(curso = año)
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})
    else:
        alumnos = Alumno.objects.all()
        return render(request, 'calificaciones/index.html',{ "alumnos": alumnos})