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
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            new_registro = (('Talia', 'Moran', 'tmoran@mail.com'),
                            ('Rita', 'Moran', 'rmoran@mail.com'))
            cursor.executemany(sentencia, new_registro)
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
