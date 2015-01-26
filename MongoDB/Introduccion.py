"""
CONECTANDOSE A UNA BASE DE DATOS

-- Conectarse a un servidor mongod

Desde una consola, iniciar la aplicacion mongo con el comando:
    mongo

mongo por defecto siempre busca un server en el puerto 27017 en
localhost.
Para conectarse a un server distinto, especificar el puerto y
host con las opciones:
    mongo --port <puerto> --host <nombre_host>

-- Seleccionar una base de datos

En cualquier momento se puede ingresar el comando
    db
para conocer la base de datos actual

Para conocer todas las bases de datos existentes en el servidor
se usa el comando:
    show dbs

Para selecciona una base de datos existente/nueva,
se usa el comando: use <nombre_db>:
    use mydb

Se puede confirmar que se selecciono la base de datos correcta
volviendo a ingresar:
    db

-- Crear una coleccion e insertar un documento

Ya con la base de datos seleccionada, crear dos documentos de la
forma:
"""
    j = { name : "mongo" }
    k = { x : 3 }
"""

Luego, mandaremos insertar estos documentos a una nueva collecion
a la que llamaremos prueba con el comando:
"""
    db.prueba.insert( j )
    db.prueba.insert( k )
"""

Para confirmar que la coleccion prueba existe, usar el comando
    show collections

Finalmente, para confirmar que los documentos existen en
prueba, usar el comando:
    db.prueba.find()

 -- Consultas a documentos especificos

Para obtener el documento k, se usa el comando:
"""
    db.prueba.find( { x : 3 } )
"""

Si se deseare un unico elemento de una coleccion, se puede usar
la funcion:
"""
    db.prueba.findOne()
"""

Tambien es posible limitar el numero de resultados de una consultas
con la funcion limit de la forma:
"""
    db.prueba.find().limit(1)
"""
"""