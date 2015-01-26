"""
Operaciones CRUD (Create, Read, Update, Delete)

INSERTAR DOCUMENTOS

-- Insertar un unico documento

La siguiente es una operacion comun donde se inserta un documento a la
coleccion inventory, la cual es creada si no existe en la BD.
"""
db.inventory.insert(
   {
     item: "ABC1",
     details: {
        model: "14Q3",
        manufacturer: "XYZ Company"
     },
     stock: [ { size: "S", qty: 25 }, { size: "M", qty: 50 } ],
     category: "clothing"
   }
)
"""
Las operacion de insert() siempre retornan un objeto del tipo
WriteResult, el cual reporta el resultado de la operacion.

Para verificar el documento recien insertado, se usa:
    db.inventory.find()

-- Insertar varios documentos a la vez

Es posible crear arreglos de documentos y mandar dicho arreglo
a la funcion insert

Por ejemplo:
"""
var mydocuments =
    [
      {
        item: "ABC2",
        details: { model: "14Q3", manufacturer: "M1 Corporation" },
        stock: [ { size: "M", qty: 50 } ],
        category: "clothing"
      },
      {
        item: "MNO2",
        details: { model: "14Q3", manufacturer: "ABC Company" },
        stock: [ { size: "S", qty: 5 }, { size: "M", qty: 5 }, { size: "L", qty: 1 } ],
        category: "clothing"
      },
      {
        item: "IJK2",
        details: { model: "14Q2", manufacturer: "M5 Corporation" },
        stock: [ { size: "S", qty: 5 }, { size: "L", qty: 1 } ],
        category: "houseware"
      }
    ];
"""

Luego se mandan insertar:
    db.inventory.insert( mydocuments )

Para estos casos, el objeto retornado para reportar los resultados se
llama BulkWriteResult


CONSULTAR DOCUMENTOS

-- Seleccionar todos los documentos de una coleccion

Se pueden usar los comandos:
    db.inventory.find( {} )
O bien:
    db.inventory.find()

-- Condiciones en la consulta

Para especificar condiciones de equivalencia en la consulta,
se colocan los campos : { <field>: <value> } dentro del documento
de consulta.

Por ejemplo:
"""
    db.inventory.find( { type: "snacks" } )
"""

-- Especificar condiciones usando operadores de consulta

Existen multiples operadores para las consultas,
para una lista completa, usar este link de la documentacion oficial
de mongodb:
http://docs.mongodb.org/manual/reference/operator/query/#query-selectors

Un ejemplo de estos operadores es:
"""
db.inventory.find( { type: { $in: [ 'food', 'snacks' ] } } )
"""

-- Especificar condicion AND

Esta condicion es agregada implicitamente cuando mas de una condicion
es agregada en el documento, por ejemplo:
"""
db.inventory.find( { type: 'food', price: { $lt: 9.95 } } )
"""

-- Especificar condicion OR

operador $or

ejemplo de consulta:
"""
db.inventory.find(
   {
     $or: [ { qty: { $gt: 100 } }, { price: { $lt: 9.95 } } ]
   }
)
"""

-- Especificar condicion AND y OR en una misma consulta

"""
db.inventory.find(
   {
     type: 'food',
     $or: [ { qty: { $gt: 100 } }, { price: { $lt: 9.95 } } ]
   }
)
"""

-- Documentos Embebidos

"""
db.inventory.find(
    {
      producer:
        {
          company: 'ABC123',
          address: '123 Street'
        }
    }
)
"""

Accesando campos de documentos embebidos
"""
db.inventory.find( { 'producer.company': 'ABC123' } )

db.inventory.find( { producer: {company: "aaaa", address:"aaa"} } )
"""


MODIFICAR DOCUMENTOS

mongodb usa la funcion update() para ejecutar modificaciones a documentos.

la funcion update acepta hasta 3 documentos como argumentos, por lo
general solo se usan, dos:
    Documento tipo consulta que define que documentos se desean
        actualizar.
    Documento donde se definen los cambios a realizar
    Documento donde se definen opciones extra para la modificacion.

-- Modificar campos especificos en un documentos
update usa "update operators", como por ejemplo "$set",
para una lista completa de operadores, consultar:
http://docs.mongodb.org/manual/reference/operator/update/

Ejemplo de update usando $set y $currentDate:
"""
db.inventory.update(
    { item: "MNO2" },
    {
      $set: {
        category: "apparel",
        details: { model: "14Q3", manufacturer: "XYZ Company" }
      },
      $currentDate: { lastModified: true }
    }
)
"""
Al igual que los insert, update retorna un WriteResult.

-- Modificar un campo embebidos
"""
db.inventory.update(
  { item: "ABC1" },
  { $set: { "details.model": "14Q2" } }
)
"""

-- Modificar multiples documentos
Por default, mongo actualiza un documento por updtade.
Para modificar mas de un documento a la vez, se manda un tercer documento:
"""
db.inventory.update(
   { category: "clothing" },
   {
     $set: { category: "apparel" },
     $currentDate: { lastModified: true }
   },
   { multi: true }
)
"""

-- Reemplazar un documento
Se logra si no se especifica ningun update operator
"""
db.inventory.update(
   { item: "BE10" },
   {
     item: "BE05",
     stock: [ { size: "S", qty: 20 }, { size: "M", qty: 5 } ],
     category: "apparel"
   }
)
"""

-- Opcion Upsert
Mongo por default no hace nada si en un update no encuentra ningun
documento que concuerte con el filtro mandado.

Pero activando la opcion upsert, mongo inserta un nuevo documento
si ninguno fue modificado.

Ejemplo:
"""
db.inventory.update(
   { item: "TBD1" },
   {
     item: "TBD1",
     details: { "model" : "14Q4", "manufacturer" : "ABC Company" },
     stock: [ { "size" : "S", "qty" : 25 } ],
     category: "houseware"
   },
   { upsert: true }
)
"""

ELIMINAR DOCUMENTOS

mongoDB usa la funcion remove() para eliminar documento.
Es posible eliminar todos lo documentos de una coleccion, eliminar
documentos especificos o eliminar solo un documento.

-- Eliminar todos los documentos

El siguiente comando elimina todos los documentos de la coleccion
    db.inventory.remove({})

-- Eliminar documentos de acuerdo a una condicion

ejemplo:
"""
db.inventory.remove( { type : "food" } )
"""
Solo se envia un documento tipo query a la funcion remove.

-- Eliminar solo un documento de acuerdo a una condicion.
Se especifica el parametro de la funcion removo justOne en true o 1.
ejemplo:
"""
db.inventory.remove( { type : "food" }, 1 )
"""

"""
