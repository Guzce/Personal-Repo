class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
        Id Persona: {self._id_persona}, 
        Nombre: {self._nombre}, 
        Apellido: {self._apellido}, 
        Email: {self._email}
        '''
    # Metodos Getters and Setters

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    persona01 = Persona(5, 'Robert', 'Travis', 'robertt@mail.com')
    print(persona01.email)
    persona01.id_persona = 8
    # persona01.email()
    print(persona01)
    # print(persona01.email)
