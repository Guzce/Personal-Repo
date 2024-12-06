from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log


class PersonaDAO:
    """
    DAO: DATA ACCES OBJECT
    CRUD: CREATE_ READ_ UPDATE_ DELETE
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def selecionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona Actualizada {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valor = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valor)
                log.debug(f'Persona Eliminada {persona}')
                return cursor.rowcount


if __name__ == '__main__':
    # LEER REGISTROS
    personas = PersonaDAO.selecionar()
    for persona in personas:
        log.debug(persona)

    # INSERTAR REGISTROS
    # persona1 = Persona(nombre='Josias', apellido='Maza', email='jmaza@mail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # ACTUALIZAR REGISTROS
    # persona1 = Persona(19, nombre='Josias', apellido='Maza', email='jmaza@mail.com')
    # persona_actualizada = PersonaDAO.actualizar(persona1)
    # log.debug(f'Persona Actualizada: {persona_actualizada}')

    # ELIMINAR REGISTROS
    # persona1 = Persona(id_persona=19)
    # persona_eliminada = PersonaDAO.eliminar(persona1)
    # log.debug(f'Persona Eliminada: {persona_eliminada}')
