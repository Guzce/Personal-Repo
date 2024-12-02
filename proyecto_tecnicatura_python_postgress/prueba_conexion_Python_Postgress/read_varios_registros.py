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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves = input("Digite los id a consultar separados por un espacio: ")
            # llaves_primarias = tuple(llaves.split(' ')),
            llaves_primarias = (1, 2),
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    conexion.close()
