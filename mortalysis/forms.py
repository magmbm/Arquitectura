from django import forms
from .models import ErrorMortal, Paciente, Defuncion
from django.core.exceptions import ValidationError
from datetime import date

class ErrorMortalForm(forms.ModelForm):
    class Meta:
        model = ErrorMortal
        fields = ['descripcion_error_mortal']
        labels = {
            'descripcion_error_mortal': "Descripción del Error Mortal",
        }
        widgets = {
            'descripcion_error_mortal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Error en medicación'}),
        }
        error_messages = {
            'descripcion_error_mortal': {
                'required': "El campo es obligatorio.",
            },
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'numrut_paciente', 'dvrut_paciente', 'p_nombre_paciente', 's_nombre_paciente',
            'a_paterno_paciente', 'a_materno_paciente', 'edad_paciente', 'genero_paciente', 'FK_id_comuna'
        ]
        labels = {
            'numrut_paciente': "Número de RUT",
            'dvrut_paciente': "Dígito Verificador",
            'p_nombre_paciente': "Primer Nombre",
            's_nombre_paciente': "Segundo Nombre",
            'a_paterno_paciente': "Apellido Paterno",
            'a_materno_paciente': "Apellido Materno",
            'edad_paciente': "Edad",
            'genero_paciente': "Género",
            'FK_id_comuna': "Comuna",
        }
        widgets = {
            'numrut_paciente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 12345678'}),
            'dvrut_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 9'}),
            'p_nombre_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Juan'}),
            's_nombre_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Carlos'}),
            'a_paterno_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Pérez'}),
            'a_materno_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Gómez'}),
            'edad_paciente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 45'}),
            'genero_paciente': forms.Select(attrs={'class': 'form-control'}, choices=[('M', 'Masculino'), ('F', 'Femenino')]),
            'FK_id_comuna': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'numrut_paciente': {
                'required': "El campo es obligatorio.",
            },
            'p_nombre_paciente': {
                'required': "El campo es obligatorio.",
            },
            'a_paterno_paciente': {
                'required': "El campo es obligatorio.",
            },
        }

class DefuncionForm(forms.ModelForm):
    class Meta:
        model = Defuncion
        fields = [
            'hora_defuncion', 'fecha_defuncion', 'FK_id_paciente', 
            'FK_id_personal_medico', 'FK_id_causa_ingreso', 'FK_id_error_mortal', 'FK_id_centro_medico'
        ]
        labels = {
            'hora_defuncion': "Hora de la Defunción",
            'fecha_defuncion': "Fecha de la Defunción",
            'FK_id_paciente': "Paciente",
            'FK_id_personal_medico': "Personal Médico Responsable",
            'FK_id_causa_ingreso': "Causa del Ingreso",
            'FK_id_error_mortal': "Error Mortal (si aplica)",
            'FK_id_centro_medico': "Centro Médico",
        }
        widgets = {
            'hora_defuncion': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'fecha_defuncion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'FK_id_paciente': forms.Select(attrs={'class': 'form-control'}),
            'FK_id_personal_medico': forms.Select(attrs={'class': 'form-control'}),
            'FK_id_causa_ingreso': forms.Select(attrs={'class': 'form-control'}),
            'FK_id_error_mortal': forms.Select(attrs={'class': 'form-control'}),
            'FK_id_centro_medico': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'fecha_defuncion': {
                'required': "El campo es obligatorio.",
            },
            'FK_id_paciente': {
                'required': "El campo es obligatorio.",
            },
        }

    def clean_fecha_defuncion(self):
        fecha_defuncion = self.cleaned_data['fecha_defuncion']
        if fecha_defuncion > date.today():
            raise ValidationError("La fecha de defunción no puede ser una fecha futura.")
        return fecha_defuncion
