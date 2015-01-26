"""
OOP:
Definiendo clases en python

"""
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
"""

"""
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
"""


Herencia
"""
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
"""

Ejemplos de clases de uso real:
Viejo estilo, usado principalmente en python 2
"""
class Comando(object):
    """Tipo de dato usado para representar el llamado de comandos EscPos
    en el archivo .ticket

    Atributos:
        @nombre: STR, nombre del comando
    """
    def __init__(self, nombre):
        self._nombre = nombre

    def __repr__(self, *args, **kwargs):
        return "Comando: "+self.nombre()

    def get_nombre(self):
        """Getter de nombre."""
        return self._nombre

    def set_nombre(self, value):
        """Setter de nombre."""
        return self._nombre = value
"""

Estilo Usual en python 3
"""
class Texto:
    """Tipo de dato usado para representar la insersion de
    texto imprimible en el archivo .ticket

    Atributos:
        @texto: STR, texto a imprimirse
        @variable: STR, variable de python contenida en el modulo
                indicado en el archivo ticket. La variable debera
                ser un objeto STR o con una implementacion
                correcta de "__str__" o "__repr__"
    """
    def __init__(self, texto, variable):
        self._texto = texto
        self._variable = variable

    def __str__(self, *args, **kwargs):
        return (
            "Texto imprimible: "+ str(self.texto()) +"| variable: "+
            str(self.variable())
        )

    @property
    def texto(self):
        return self._texto
    @texto.setter
    def texto(self, value):
        self._texto = value

    @property
    def variable(self):
        return self._variable
    @variable.setter
    def variable(self, value):
        self._variable = value
"""

"""