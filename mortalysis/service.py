import mysql.connector as my_conn
from .models import CentroMedico, Region, Comuna

conexion= my_conn.connect(
    host= 'localhost',
    password= 'contrA-123',
    user= 'root',
    database= 'MINSAL_PRUEBA'
)



cursor= conexion.cursor()

cursor.execute("SELECT * FROM REGION")

def get_region():
    for i in (cursor):
        region= Region(id_region= i[0], nombre_region= i[1])
        region.save()

cursor.execute("SELECT * FROM COMUNA")

def get_comuna():
    for i in (cursor):
        comuna= Comuna(id_comuna= i[0], nombre_comuna= i[1], FK_id_region= i[2])
        comuna.save()

cursor.close()

    
"""def get_centro_medico():
    
    for i in (cursor):
        centro= CentroMedico(id_centro_medico= i[0], nombre_centro_med= i[1], direccion_centro_med= i[2], FK_id_comuna= i[3])    
        centro.save()
"""
