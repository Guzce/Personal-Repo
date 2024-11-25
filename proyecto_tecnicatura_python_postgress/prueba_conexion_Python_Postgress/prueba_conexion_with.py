"""
Uso del context manager with
/no sera necesario cerrar el cursor
/se recomientda uso de try/except/finally
/cierre de conexion en finally
"""
import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)

    registros = cursor.fetchall()
    print(registros)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
