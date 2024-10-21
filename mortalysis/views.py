from django.shortcuts import render
from . import models

from .service import get_region, get_comuna, cursor, get_centro_medico


from django.shortcuts import render, get_object_or_404, redirect
from .models import ErrorMortal, Paciente, Defuncion
from .forms import ErrorMortalForm, PacienteForm, DefuncionForm

# Create your views here.

def analisis(request):
    if request.method== "GET":
        context={
            'clase':'analisis'
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
