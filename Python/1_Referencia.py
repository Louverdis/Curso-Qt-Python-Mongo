"""
INTRODUCCION

"""
---------------------------------------------------------------------------
# Python 3: Simple output (with Unicode)
>>> print("Hello, I'm Python!")
Hello, Im Python!

# Input, assignment
>>> name = input('What is your name?\n')
>>> print('Hi, %s.' % name)
What is your name?
Python
Hi, Python.
---------------------------------------------------------------------------
"""

** Tipos Nativos **

*Numeric Types — int, float, complex

*Sequence Types — list, tuple, range

Operaciones soportadas:
Operation                           Result
x in s ------------------ True if an item of s is equal to x, else False
x not in s -------------- False if an item of s is equal to x, else True
s + t ------------------- the concatenation of s and t
s * n or n * s ---------- n shallow copies of s concatenated
s[i] -------------------- ith item of s, origin 0
s[i:j] ------------------ slice of s from i to j
s[i:j:k] ---------------- slice of s from i to j with step k
len(s) ------------------ length of s
min(s) ------------------ smallest item of s
max(s) ------------------ largest item of s
s.index(x[, i[, j]]) ---- index of the first occurrence of x in s (at or after index i and before index j)
s.count(x) -------------- total number of occurrences of x in s

--Lists
Formas de construir una lista:

Usando parentesis cuadrados:
    list = []
Definiendo contenido dentro de parentesis cuadrados:
    list = [a], [a, b, c]
Usando una compresion de listas:
    list = [x for x in iterable]
Usando su contructor:
    list() or list(iterable)

Metodos disponibles para las listas:
list.append(x) ----- appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
list.clear() ------- removes all items from s (same as del s[:])
list.copy() -------- creates a shallow copy of s (same as s[:])
list.extend(t) ----- extends s with the contents of t (same as s[len(s):len(s)] = t)
list.insert(i, x) -- inserts x into s at the index given by i (same as s[i:i] = [x])
list.pop([i]) ------ retrieves the item at i and also removes it from s
list.remove(x) ----- remove the first item from s where s[i] == x
list.reverse() ----- reverses the items of s in place

--Tuples
Formas de construir una tupla:

Con parentesis, denotando una tupla vacia:
    tuple = ()
Definiendo sus contenidos entre parentesis:
    tuple = (a,...)
Usando su constructor:
    tuple = tuple() or tuple(iterable)

--Ranges
Secuencias inmutables numericas.
Se construyen mediante el constructor:
    range(stop)
    range(start, stop[, step])

Ejemplos:
"""
---------------------------------------------------------------------------
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
---------------------------------------------------------------------------
"""
*Mapping Types — dict

--dict
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

Se pueden definir con corchetes:
    dic = {}

El modo de definir sus contenidos es:
    dic = {"llave": valor, .....}

O usando sus constructores

Ejemplos de modos de contruir un diccionario
con los valores: {"one": 1, "two": 2, "three": 3}

"""
---------------------------------------------------------------------------
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
---------------------------------------------------------------------------
"""
---------------------------------------------------------------------------

** Flujo del programa

"""
---------------------------------------------------------------------------
# For loop on a list
>>> numbers = [2, 4, 6, 8]
>>> product = 1
>>> for number in numbers:
...    product = product * number
...
>>> print('The product is:', product)
The product is: 384
---------------------------------------------------------------------------
"""

Los controles de flujo generales estan en python

-if Statements

"""
---------------------------------------------------------------------------
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')

-for Statements
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
---------------------------------------------------------------------------
"""

-The range() function
"""
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
"""

-break and continue Statements, and else Clauses on Loops
"""
---------------------------------------------------------------------------
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

-pass Statements
>>> def func():
...     pass
...
---------------------------------------------------------------------------
"""
---------------------------------------------------------------------------
** Definiendo funciones **

"""
---------------------------------------------------------------------------
>>> def fib(n):    # write Fibonacci series up to n
...     #Print a Fibonacci series up to n.
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
---------------------------------------------------------------------------
"""

La sintaxis para definir una funcion es:
Se usa la palabra reservada """def"""" seguido de los siguientes datos:
"""
def nombre_funcion(argument, keyword_argument=0, *args, **kwargs):
    #Cuerpo de la funcion
    pass
"""

-Argumentos posicionales
Argumentos regulares de una funcion, definidos de la forma:
"""
def funcion(a, b, c):
    pass
"""

-Keyword arguments
Argumentos identificados por una llave, su posicion no es importante
a la hora de llamar a la funcion.
Se usan de la forma:
"""
def funcion(a=1, b=2, c=3):
    pass
"""

-Listas de argumentos arbitraria
Es posible definir funciones que tomen una cantidad arbitraria de
argumentos posicionales.
Esto se consigue con la forma:
"""
def funcion(*args):
    pass
"""
Estas funciones toman una cantidad arbitraria de argumentos, como por
ejemplo: """funcion(1,2,3,4,5)"""

O bien, pueden tomar directamente una lista y usar sus contenidos como
argumentos.

Una funcion de ejemplo:
"""
---------------------------------------------------------------------------
>>> def concat(*args, sep="/"):
...    return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
---------------------------------------------------------------------------
"""

** Expresiones lambda
Estas expresiones son pequeñas funciones anonimas.
Las funciones definidas mediante lambda estan restringidas a una sola
linea.

Se definan con la forma:
"""
lambda a, b: a+b
"""
Estas funciones siempre retornan el resultado de la expresion en su cuerpo

Ejemplo:
"""
---------------------------------------------------------------------------
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
---------------------------------------------------------------------------
"""




"""