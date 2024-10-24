from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=45, null=False, blank=False)

    def __str__(self):
        return str(self.nombre_region)

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=60, null=False, blank=False)
    FK_id_region = models.ForeignKey(Region, on_delete=models.CASCADE, default=1, db_column='id_region')

    def __str__(self):
        return str(self.nombre_comuna)

class CausaIngreso(models.Model):
    id_causa_ingreso = models.IntegerField(primary_key=True)
    descripcion_causa_ingreso = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return str(self.descripcion_causa_ingreso)

class ErrorMortal(models.Model):
    id_error_mortal = models.IntegerField(primary_key=True)
    descripcion_error_mortal = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return str(self.descripcion_error_mortal)

class CentroMedico(models.Model):
    id_centro_medico = models.IntegerField(primary_key=True)
    nombre_centro_med = models.CharField(max_length=80, null=False, blank=False)
    direccion_centro_med = models.CharField(max_length=60, null=False, blank=False)
    FK_id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=1, db_column='id_comuna')

    def __str__(self):
        return str(self.nombre_centro_med)

class PersonalMedico(models.Model):
    id_personal_med = models.IntegerField(primary_key=True)
    numrut_pers_med = models.IntegerField(null=False, blank=False, default=0)
    dvrut_pers_med = models.CharField(max_length=1, null=False, blank=False)
    p_nombre_pers_med = models.CharField(max_length=60, null=False, blank=False)
    s_nombre_pers_med = models.CharField(max_length=60, null= True)
    a_paterno_pers_med = models.CharField(max_length=60, null=False, blank=False)
    a_materno_pers_med = models.CharField(max_length=60, null=False, blank=False)
    cargo_pers_med = models.CharField(max_length=50, null=False, blank=False)
    edad_pers_med = models.IntegerField(null=False, blank=False, default=0)
    anios_experiencia = models.IntegerField(null=False, blank=False, default=0)
    FK_id_centro_medico = models.ForeignKey(CentroMedico, on_delete=models.CASCADE, default=1, db_column='id_centro_medico')

    def __str__(self):
        return f"{self.p_nombre_pers_med} {self.a_paterno_pers_med} {self.a_materno_pers_med}"

class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    numrut_paciente = models.IntegerField(null=False, blank=False, default=0)
    dvrut_paciente = models.CharField(max_length=1, null=False, blank=False)
    p_nombre_paciente = models.CharField(max_length=60, null=False, blank=False)
    s_nombre_paciente = models.CharField(max_length=60, null=False, blank=False)
    a_paterno_paciente = models.CharField(max_length=60, null=False, blank=False)
    a_materno_paciente = models.CharField(max_length=60, null=False, blank=False)
    edad_paciente = models.IntegerField(null=False, blank=False, default=0)
    genero_paciente = models.CharField(max_length=1, null=False, blank=False)
    FK_id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=1, db_column='id_comuna')

    def __str__(self):
        return f"{self.p_nombre_paciente} {self.a_paterno_paciente} {self.a_materno_paciente}"

class Defuncion(models.Model):
    id_defuncion = models.IntegerField(primary_key=True)
    hora_defuncion = models.TimeField(null=True)
    fecha_defuncion = models.DateField(null=False, blank=False)
    FK_id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=1, db_column='id_paciente')
    FK_id_personal_medico = models.ForeignKey(PersonalMedico, on_delete=models.CASCADE, default=1, db_column='id_personal_medico')
    FK_id_causa_ingreso = models.ForeignKey(CausaIngreso, on_delete=models.CASCADE, default=1, db_column='id_causa_ingreso')
    FK_id_error_mortal = models.ForeignKey(ErrorMortal, on_delete=models.CASCADE, default=1, db_column='id_error_mortal')
    FK_id_centro_medico = models.ForeignKey(CentroMedico, on_delete=models.CASCADE, default=1, db_column='id_centro_medico')

    def __str__(self):
        return f"Defunción {self.id_defuncion} - {self.FK_id_paciente}"

# Uncomment and update if needed
# class USUARIO(models.Model):
#     usuario_FK = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=60, null=False)
#     s_nombre = models.CharField(max_length=60, null=True)
#     appaterno = models.CharField(max_length=60, null=False)
#     apmaterno = models.CharField(max_length=60, null=False)
