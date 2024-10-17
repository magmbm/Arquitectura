from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class REGION(models.Model):
    id_region= models.IntegerField(primary_key= True)
    nombre= models.CharField(max_length= 45)

class COMUNA(models.Model):
    id_comuna= models.IntegerField(primary_key= True)
    nombre= models.CharField(max_length=60)
    region_FK= models.ForeignKey(REGION, on_delete=models.CASCADE)

class USUARIO(models.Model):
    usuario_FK= models.OneToOneField(User, primary_key= True, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=60, null=False)
    s_nombre= models.CharField(max_length= 60, null= True)
    appaterno= models.CharField(max_length= 60, null= False)
    apmaterno= models.CharField(max_length= 60, null= False)


class CAUSA_MUERTE(models.Model):
    id_causa_muerte= models.IntegerField(primary_key= True)
    causa_desc= models.CharField(max_length= 80)

class CENTRO_MEDICO(models.Model):
    id_centro_med= models.IntegerField(primary_key= True) 
    nombre= models.CharField(max_length= 80)
    direccion= models.CharField(max_length= 60)
    comuna_FK= models.ForeignKey(COMUNA, on_delete=models.CASCADE)

class PERSONAL_MEDICO(models.Model):
    id_personal= models.IntegerField(primary_key= True)
    nombre= models.CharField(max_length= 60)
    s_nombre= models.CharField(max_length= 60)
    appaterno= models.CharField(max_length= 60)
    apmaterno= models.CharField(max_length= 60)
    numrut= models.IntegerField(max_length= 11)
    dvrut= models.CharField(max_length= 1)
    profesion= models.CharField(max_length= 50)
    edad= models.IntegerField()
    anios_de_trabajo= models.IntegerField()
    anios_en_el_centro= models.IntegerField()
    centro_medico_FK= models.ForeignKey(CENTRO_MEDICO, on_delete=models.CASCADE)

class PACIENTE(models.Model):
    id_paciente= models.IntegerField(primary_key= True)
    p_nombre= models.CharField(max_length= 60)
    s_nombre= models.CharField(max_length= 60)
    appaterno= models.CharField(max_length= 60)
    apmaterno= models.CharField(max_length= 60)
    numrut= models.IntegerField(max_length= 11)
    dvrut= models.CharField(max_length= 1)
    edad= models.IntegerField(max_length= 120)
    genero= models.CharField(max_length= 1)
    comuna_FK= models.ForeignKey(COMUNA, on_delete=models.CASCADE)

class DEFUNCION(models.Model):
    id_defuncion= models.IntegerField(primary_key= True)
    hora_muerte= models.TimeField(null= True)
    dia_muerte= models.DateField()
    paciente= models.ForeignKey(PACIENTE, on_delete=models.CASCADE)
    personal_medico= models.ForeignKey(PERSONAL_MEDICO, on_delete=models.CASCADE)
    centro_medico= models.ForeignKey(CENTRO_MEDICO, on_delete=models.CASCADE) 
    causa_muerte= models.ForeignKey(CAUSA_MUERTE, on_delete=models.CASCADE)
