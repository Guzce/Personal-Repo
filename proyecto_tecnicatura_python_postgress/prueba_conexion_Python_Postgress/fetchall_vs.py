import psycopg2
#  FETCHONE() /De acuerdo al tipo de consulta /caso de registro individual
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
"""try:
    with conexion:
        with conexion.cursor() as cursor:
            # uso de IN en el query y registros a consultar
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2)'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()"""
# Ahora usando parametros placeholder
try:
    with conexion:
        with conexion.cursor() as cursor:
            # uso de IN en el query y registros a consultar
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # pasamos una tupla como parametro
            # llaves_primarias = ((),) /tupla de tupla
            llaves = input("Digite los id a consultar separados por un espacio: ")
            llaves_primarias = (tuple(llaves.split(' ')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
