from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.USUARIO)
admin.site.register(models.CAUSA_MUERTE)
admin.site.register(models.CENTRO_MEDICO)
admin.site.register(models.COMUNA)
admin.site.register(models.REGION)
admin.site.register(models.DEFUNCION)
admin.site.register(models.PACIENTE)
admin.site.register(models.PERSONAL_MEDICO)