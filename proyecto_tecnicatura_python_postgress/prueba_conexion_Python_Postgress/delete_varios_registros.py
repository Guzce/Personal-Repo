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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            valor = (13, 18),
            cursor.execute(sentencia, valor)
            registro_eliminados = cursor.rowcount
            print(registro_eliminados)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
