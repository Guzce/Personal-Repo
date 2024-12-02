"""
* pip install psycopg2 /usaremos el siguiente comando en terminal
para importar los recursos de conexion
* importante ubicarse en la carpeta raiz del proyecto
"""
import psycopg2  # Libreria encargado de gestionar conexion a la base de datos

# Asignamos metodo .connect() de psycopg2 a una variable encargada de la conexion
"""
El metodo recibe **kwargs diccionario con valores  de longitud variables
"""
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

# Crecion de una variable cursor encargada de ejecutar sentencias query
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)  # metodo execute recibe y ejecuta la consulta query
# Para poder recuperar los registros usamos el metodo fetchall() del metodo cursor()
registros = cursor.fetchall()
print(registros)

# es importante cerrar ambos procesos con sus respectivos métodos
cursor.close()
conexion.close()
