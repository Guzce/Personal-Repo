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
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            valor = (7,)
            cursor.execute(sentencia, valor)
            registro_eliminado = cursor.rowcount
            print(registro_eliminado)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
