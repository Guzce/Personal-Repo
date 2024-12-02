import psycopg2
#  FETCHONE() /De acuerdo al tipo de consulta /caso de registro individual
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
            # sentencia = 'SELECT * FROM persona WHERE id_persona = 1'
            # %s placeholder /lo usamos para pasar un parametro
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = int(input("Digite el id que desea consultar: "))
            # Ahora es importante pasar una tupla luego de la sentencia con el parametro del placeholder a execute()
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
