from django.contrib import admin
from . import models

# Register your models here.

#admin.site.register(models.USUARIO)
admin.site.register(models.Region)
admin.site.register(models.Comuna)
admin.site.register(models.CausaIngreso)
admin.site.register(models.ErrorMortal)
admin.site.register(models.CentroMedico)
admin.site.register(models.PersonalMedico)
admin.site.register(models.Paciente)
admin.site.register(models.Defuncion)