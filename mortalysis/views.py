from django.shortcuts import render
from . import models

import pandas as pd

from .service import get_region, get_comuna, cursor, get_centro_medico


from django.shortcuts import render, get_object_or_404, redirect
from .models import ErrorMortal, Paciente, Defuncion
from .forms import ErrorMortalForm, PacienteForm, DefuncionForm
from django.apps import apps

# Create your views here.


def get_context_analisis(key, dict):
    modelo= dict.get(key)
    results= modelo.objects.all()
    arr=[]
    context={}
    total_datos= 0
    if key== "1":
        for i in results:
            dic={
                'p': i.id_centro_medico,
                'nombre': i.nombre_centro_med,
                'direccion': i.direccion_centro_med,
                'comuna': i.FK_id_comuna.nombre_comuna
            }
            arr.append(dic)
        df= pd.DataFrame(arr, columns=('p', 'nombre', 'direccion', 'comuna'))
        variables= [ 
                    {
                    'Titulo': 'NOMBRE',
                    'Moda': df['nombre'].mode(),
                    'Mediana': 'N/A',
                    'Media': 'N/A',
                    'Desvest': 'N/A',
                    'Coeficiente': 'N/A',
                    'Rango':'N/A'
                    }, 
                    {
                    'Titulo': 'DIRECCIÓN',
                    'Moda': 'N/A',
                    'Mediana': 'N/A',
                    'Media': 'N/A',
                    'Desvest': 'N/A',
                    'Coeficiente': 'N/A',
                    'Rango':'N/A'
                    }, 
                    {
                    'Titulo': 'COMUNA',
                    'Moda': df['comuna'].mode(),
                    'Mediana': 'N/A',
                    'Media': 'N/A',
                    'Desvest': 'N/A',
                    'Coeficiente': 'N/A',
                    'Rango':'N/A'
                    }
                    ]
        context['variables']= variables
        total_datos= len(arr)
        context['total_datos']= total_datos
    elif key=="2":
        for i in results:
            dic={
                'p': i.id_personal_med,
                'numrut': i.numrut_pers_med,
                'dvrut' : i.dvrut_pers_med,
                'p_nombre': i.p_nombre_pers_med,
                's_nombre': i.s_nombre_pers_med,
                'appaterno': i.a_paterno_pers_med,
                'apmaterno': i.a_materno_pers_med,
                'cargo': i.cargo_pers_med,
                'edad': i.edad_pers_med,
                'anios_exp' : i.anios_experiencia,
                'centro' : i.FK_id_centro_medico
            }
            arr.append(dic)
        df= pd.DataFrame(arr, columns=(
                'p', 'numrut', 'dvrut', 'p_nombre', 's_nombre', 
                'appaterno', 'apmaterno', 'cargo', 'edad', 
                'anios_exp', 'centro')
                )
        variables= [ 
            {
            'Titulo': 'NUMRUT',
            'Moda': 'N/A',
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            }, 
            {
            'Titulo': 'DVRUT',
            'Moda': df['dvrut'].mode,
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            }, 
            {
            'Titulo': 'PRIMER NOMBRE',
            'Moda': df['p_nombre'].mode(),
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            },
            {
            'Titulo': 'SEGUNDO NOMBRE',
            'Moda': df['s_nombre'].mode,
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            },
            {
            'Titulo': 'PRIMER APELLIDO',
            'Moda': df['appaterno'].mode(),
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            },
            {
            'Titulo': 'SEGUNDO APELLIDO',
            'Moda': df['apmaterno'].mode(),
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            },
            {
            'Titulo': 'CARGO',
            'Moda': df['cargo'].mode(),
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            },
            {
            'Titulo': 'EDAD',
            'Moda': df['edad'].mode(),
            'Mediana': df['edad'].median,
            'Media': df['edad'].mean,
            'Desvest': df['edad'].std,
            'Coeficiente': (df['edad'].std/ df['edad'].mean),
            'Rango': df['edad'].max - df['edad'].min
            },
            {
            'Titulo': 'AÑOS DE EXPERIENCIA',
            'Moda': df['anios_exp'].mode(),
            'Mediana': df['anios_exp'].median(),
            'Media': df['anios_exp'].mean(),
            'Desvest': df['anios_exp'].std,
            'Coeficiente': (df['anios_exp'].std/ df['anios_exp'].mean),
            'Rango': df['anios_exp'].max - df['anios_exp'].min
            },
            {
            'Titulo': 'CENTRO MEDICO',
            'Moda': df['centro'].mode(),
            'Mediana': 'N/A',
            'Media': 'N/A',
            'Desvest': 'N/A',
            'Coeficiente': 'N/A',
            'Rango':'N/A'
            },
        ]
        context['variables']= variables
        total_datos= len(arr)
        context['total_datos']= total_datos
    elif key== "3":
        for i in results:
            dic={
                'p': i.id_error_mortal,
                'descripcion': i.descripcion_error_mortal
            }

            arr.append(dic)
        df= pd.DataFrame(arr, columns=('p', 'descripcion'))
        variables=[
                {
                'Titulo': 'CAUSA DE MUERTE',
                'Moda': df['descripcion'].mode,
                'Mediana': 'N/A',
                'Media': 'N/A',
                'Desvest': 'N/A',
                'Coeficiente': 'N/A',
                'Rango':'N/A'
                },
                
        ]
        context['variables']= variables
        total_datos= len(arr)
        context['total_datos']= total_datos
    elif key== "4":
        for i in results:
            dic={
                'p': i.id_defuncion,
                'causa': i.FK_id_causa_ingreso.descripcion_causa_ingreso, 
            }
            arr.append(dic)
        df= pd.DataFrame(arr, columns=('p', 'causa'))
        variables=[
                {
                'Titulo': 'CAUSA DE INGRESO',
                'Moda': df['causa'].loc[0],
                'Mediana': 'N/A',
                'Media': 'N/A',
                'Desvest': 'N/A',
                'Coeficiente': 'N/A',
                'Rango':'N/A'
                },
        ]
        context['variables']= variables
        total_datos= len(arr)
        context['total_datos']= total_datos
    return context

def analisis(request):
    if request.method== "POST":
        variable= request.POST["variable"]
        modelo_codigo= {
            "1": models.CentroMedico,
            "2": models.PersonalMedico,
            "3": models.Defuncion,
            "4": models.Defuncion,
            "5": [models.Region, models.Comuna],
             
        }
        context= get_context_analisis(variable, modelo_codigo)
        return render(request, "mortalysis/analisis.html", context)
    else:
        context={
            'clase':'analisis',
            'centro': "1",
            'personal': "2",
            'error': "3",
            'causa': "4",
            'ubicacion' : "5"
        }
        return render(request, "mortalysis/analisis.html", context)

def index(request):
    try:
        get_region()
        get_comuna()
        get_centro_medico()
        cursor.close()
    except:
        print("Error")
    context = {
        'clase':'index',
    }
    return render(request, "mortalysis/index.html", context)

# Listar Errores Mortales
def listar_errores_mortales(request):
    errores_mortales = ErrorMortal.objects.all().order_by('descripcion_error_mortal')
    context = {'errores_mortales': errores_mortales, 'clase': 'mantenedores'}
    return render(request, 'mortalysis/errores_mortales.html', context)

# Agregar un Error Mortal
def registrar_error_mortal(request):
    if request.method == "POST":
        form = ErrorMortalForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('descripcion_error_mortal')
            mensaje = f"{nombre} ha sido agregado exitosamente"
            return render(request, 'mortalysis/registrar_error_mortal.html', {'form': ErrorMortalForm(), 'mensaje': mensaje, 'clase': 'mantenedores'})
    else:
        form = ErrorMortalForm()
    return render(request, 'mortalysis/registrar_error_mortal.html', {'form': form, 'clase': 'mantenedores'})

# Editar un Error Mortal
def editar_error_mortal(request, pk):
    error_mortal = get_object_or_404(ErrorMortal, id_error_mortal=pk)
    if request.method == "POST":
        form = ErrorMortalForm(request.POST, instance=error_mortal)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos de {error_mortal.descripcion_error_mortal} han sido actualizados exitosamente"
            return render(request, 'mortalysis/editar_error_mortal.html', {'error_mortal': error_mortal, 'mensaje': mensaje, 'form': form, 'clase': 'mantenedores'})
    else:
        form = ErrorMortalForm(instance=error_mortal)
    return render(request, 'mortalysis/editar_error_mortal.html', {'error_mortal': error_mortal, 'form': form, 'clase': 'mantenedores'})

# Eliminar un Error Mortal
def eliminar_error_mortal(request, pk):
    try:
        error_mortal = get_object_or_404(ErrorMortal, id_error_mortal=pk)
        error_mortal.delete()
        mensaje = f"{error_mortal.descripcion_error_mortal} ha sido eliminado"
    except:
        mensaje = f"ERROR: el id {pk} no existe"
    context = {'mensaje': mensaje, 'errores_mortales': ErrorMortal.objects.all().order_by('descripcion_error_mortal'), 'clase': 'mantenedores'}
    return render(request, 'mortalysis/errores_mortales.html', context)

# Listar Pacientes
def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by('p_nombre_paciente')
    context = {'pacientes': pacientes, 'clase': 'mantenedores'}
    return render(request, 'mortalysis/pacientes.html', context)

# Registrar un Paciente
def registrar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('p_nombre_paciente')
            mensaje = f"{nombre} ha sido agregado exitosamente"
            return render(request, 'mortalysis/registrar_paciente.html', {'form': PacienteForm(), 'mensaje': mensaje, 'clase': 'mantenedores'})
    else:
        form = PacienteForm()
    return render(request, 'mortalysis/registrar_paciente.html', {'form': form, 'clase': 'mantenedores'})

# Editar un Paciente
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, id_paciente=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            mensaje = f"Los datos de {paciente.p_nombre_paciente} han sido actualizados exitosamente"
            return render(request, 'mortalysis/editar_paciente.html', {'paciente': paciente, 'mensaje': mensaje, 'form': form, 'clase': 'mantenedores'})
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'mortalysis/editar_paciente.html', {'paciente': paciente, 'form': form, 'clase': 'mantenedores'})

# Eliminar un Paciente
def eliminar_paciente(request, pk):
    try:
        paciente = get_object_or_404(Paciente, id_paciente=pk)
        paciente.delete()
        mensaje = f"{paciente.p_nombre_paciente} ha sido eliminado"
    except:
        mensaje = f"ERROR: el id {pk} no existe"
    context = {'mensaje': mensaje, 'pacientes': Paciente.objects.all().order_by('p_nombre_paciente'), 'clase': 'mantenedores'}
    return render(request, 'mortalysis/pacientes.html', context)

# Listar Defunciones
def listar_defunciones(request):
    defunciones = Defuncion.objects.all().order_by('fecha_defuncion')
    context = {'defunciones': defunciones, 'clase': 'mantenedores'}
    return render(request, 'mortalysis/defunciones.html', context)

# Registrar una Defunción
def registrar_defuncion(request):
    if request.method == "POST":
        form = DefuncionForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "La defunción ha sido registrada exitosamente"
            return render(request, 'mortalysis/registrar_defuncion.html', {'form': DefuncionForm(), 'mensaje': mensaje, 'clase': 'mantenedores'})
    else:
        form = DefuncionForm()
    return render(request, 'mortalysis/registrar_defuncion.html', {'form': form, 'clase': 'mantenedores'})

# Editar una Defunción
def editar_defuncion(request, pk):
    defuncion = get_object_or_404(Defuncion, id_defuncion=pk)
    if request.method == "POST":
        form = DefuncionForm(request.POST, instance=defuncion)
        if form.is_valid():
            form.save()
            mensaje = f"La defunción del paciente {defuncion.FK_id_paciente} ha sido actualizada exitosamente"
            return render(request, 'mortalysis/editar_defuncion.html', {'defuncion': defuncion, 'mensaje': mensaje, 'form': form, 'clase': 'mantenedores'})
    else:
        form = DefuncionForm(instance=defuncion)
    return render(request, 'mortalysis/editar_defuncion.html', {'defuncion': defuncion, 'form': form, 'clase': 'mantenedores'})

# Eliminar una Defunción
def eliminar_defuncion(request, pk):
    try:
        defuncion = get_object_or_404(Defuncion, id_defuncion=pk)
        defuncion.delete()
        mensaje = f"La defunción del paciente {defuncion.FK_id_paciente} ha sido eliminada"
    except:
        mensaje = f"ERROR: la defunción con id {pk} no existe"
    context = {'mensaje': mensaje, 'defunciones': Defuncion.objects.all().order_by('fecha_defuncion'), 'clase': 'mantenedores'}
    return render(request, 'mortalysis/defunciones.html', context)
