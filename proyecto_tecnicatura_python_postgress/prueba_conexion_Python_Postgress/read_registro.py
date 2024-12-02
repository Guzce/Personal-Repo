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
            sentencia = 'SELECT * FROM persona WHERE id_persona=%s'
            llave = input('Introduce un valor para consultar su correspondiente registro: ')
            cursor.execute(sentencia, llave)
            registro = cursor.fetchone()
            print(registro)
except Exception as e:
    print(f'Ha ocurrido un error {e}')
finally:
    conexion.close()
