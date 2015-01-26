"""
DOCUMENTACION DEL API:
http://api.mongodb.org/python/current/api/index.html


**Usando el driver de python

Para obtener una conecion a un server mongo, primero se importa el la
clase MongoClient

"""
from pymongo import MongoClient
"""
Las objetos MongoClient funcionan como instancias del programa mongo en
shell

por default, el constructor genera una conexion a un server local.

"""
client = MongoClient()
# Especificando un server
client = MongoClient('localhost', 27017)
# Especificando un server con una URI
client = MongoClient('mongodb://localhost:27017/')
"""
Para conectarse a una base de datos, se puede acceder a ella como
un atributo del objeto, o como si se accesara el valor de un dict.

"""
db = cliente.mydb
#o bien
db = cliente['mydb']
"""

Las colecciones se acceden desde la db de la misma forma

"""
coleccion = db.mi_coleccion
# o bien
coleccion = db['mi_coleccion']
"""

Dentro de python, se pueden crear colecciones y DBs de la misma
forma que en mongo.
"""
nueva_db = cliente.nueva_db
# o bien
nueva_db = cliente['nueva_db']

nueva_coleccion = nueva_db.nueva_coleccion
# o bien
nueva_coleccion = nueva_db['nueva_coleccion']

# Es pocible recortar esto a
nueva_coleccion = cliente.nueva_db.nueva_coleccion
"""

Las operaciones CRUD estan disponibles como metodos de los objetos
coleccion, poseen los mismos nombres, y funcionan igual, que en shell mongo.

"""
# Insertar
coleccion.insert({})

# Consultas
coleccion.find({})
coleccion.find_one()

# Modificaciones
coleccion.update({}, {})

# Eliminaciones
coleccion.remove({})
"""

Definicion de un grupo de clases encargadas de controlar la creacion y
el acceso a colecciones en mongoDB

"""
from pymongo import MongoClient

class Singleton(object):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases,dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class Conexion:
    __metaclass__ = Singleton

    def __init__(self, coleccion, db="mydb"):
        self._client = MongoClient()
        self._db = self.client[db]
        self._coleccion = self.db[coleccion]

    @property
    def client(self):
        return self._client

    @property
    def db(self):
        return self._db

    @property
    def coleccion(self):
        return self._coleccion

"""
"""