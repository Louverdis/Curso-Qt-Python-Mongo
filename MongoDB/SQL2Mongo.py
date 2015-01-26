"""
Mapeo de operacion entre SQL y MongoDB

Documentacion completa:
http://docs.mongodb.org/manual/reference/sql-comparison/

Terminologia y conceptos

---------------------------------------------------------------------------
SQL Terms/Concepts              MongoDB Terms/Concepts
---------------------------------------------------------------------------
database                            database

table                               collection

row                                 document or BSON document

column                              field

index                               index

table joins                         embedded documents and linking

primary key                         primary key

Specify any unique                  In MongoDB, the primary key is
column or column combination        automatically set to the _id field.
as primary key.

aggregation (e.g. group by)         aggregation pipeline
---------------------------------------------------------------------------

"""