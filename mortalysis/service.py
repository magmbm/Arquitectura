import mysql.connector as my_conn
from mortalysis.models import CentroMedico, Comuna, Region

conexion= my_conn.connect(
    host= 'localhost',
    password= 'contrA-123',
    user= 'root',
    database= 'MINSAL_PRUEBA'
)



cursor= conexion.cursor()


def get_region():
    cursor.execute("SELECT * FROM REGION")
    for i in (cursor):
        region= Region(id_region= i[0], nombre_region= i[1])
        region.save()

def get_comuna():
    cursor.execute("SELECT id_comuna, nombre_comuna, region_FK FROM COMUNA")
    for i in (cursor):
        region= Region.objects.get(id_region= i[2])
        comuna= Comuna(id_comuna= i[0], nombre_comuna= i[1], FK_id_region= region)
        comuna.save()

def get_centro_medico():
    cursor.execute("SELECT id_centro_med, nombre, direccion, comuna_FK FROM CENTRO_MEDICO")
    for i in (cursor):
        comuna= Comuna.objects.get(id_comuna= i[3])
        centro= CentroMedico(id_centro_medico= i[0], nombre_centro_med= i[1], direccion_centro_med= i[2], FK_id_comuna= comuna)    
        centro.save()

