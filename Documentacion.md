# Programacion

## Break
break permite detener un bucle antes de tiempo. Cuando se alcanza la instrucción break, saldrá inmediatamente del bucle más interno y comenzará a ejecutar el código después del bucle.

for i in range(10):
	break
print(i)

Esto imprime 0 porque i es 0 en la primera iteración del bucle y luego la instrucción break termina el bucle.

También funciona en bucles while.

while True:
	if can_harvest():
		break

Este código ejecuta el bucle while hasta que can_harvest() sea True. 
Tiene el mismo efecto que

while not can_harvest():
	pass

En bucles anidados, break siempre sale del bucle más interno.

for i in range(10):
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")


## Depuración
A veces tu código simplemente no funciona y necesitas averiguar por qué. Hay un par de herramientas para ayudarte a hacerlo.

La primera es ejecutar el programa paso a paso. 
Puedes entrar en el modo paso a paso con el botón junto al botón Ejecutar o estableciendo un punto de interrupción.

Los puntos de interrupción se pueden añadir haciendo clic en el panel de puntos de interrupción a la izquierda del código.
Cuando la ejecución llega a la línea donde está el punto de interrupción, cambiará automáticamente al modo paso a paso.

Cuando mueves el ratón sobre una variable, se muestra su valor actual.

La función print() también puede ser muy útil. Escribirá cualquier valor que se le pase directamente en el aire.

Ejemplos:

Imprime "0.24".
print(0.24)


Imprime "True" o "False".
print(can_harvest())


Imprime la posición actual.
print(get_pos_x(), get_pos_y())

La función print imprime el valor directamente en el aire y en la página de [Salida]().

Escribir en el aire a veces puede ser un poco lento si quieres imprimir muchos valores.
En este caso, puedes usar la función quick_print(), que imprime solo en la ventana de salida.

La ventana de salida también registra advertencias y errores, por lo que si algo no funciona como se esperaba, puede ser útil revisarla.

Cuando la ejecución se detiene, la salida también se escribe en el archivo output.txt en la carpeta del juego.[output.txt]().

## Comentarios
Los comentarios son partes del código que se ignoran durante la ejecución.
Se pueden añadir comentarios usando #. Cualquier cosa en la misma línea después del # es un comentario y será ignorada.

#esto es un comentario

Esto puede ser útil para añadir notas al código, y también para desactivar temporalmente partes del código sin eliminarlas.

Cualquier comentario en la línea anterior a la definición de una función será parte de la información emergente que aparece cuando pasas el ratón sobre el nombre de la función.
#Esta función no hace nada.

def f():
    pass


## Continue
continue permite detener la iteración actual de un bucle y saltar a la siguiente iteración del bucle más interno.

for i in range(10):
	continue
    print("this is never printed")


Esto ejecuta las 10 iteraciones del bucle, pero la instrucción print después de continue siempre se salta.

También funciona en bucles while.

while True:
	if not can_harvest():
		continue
    
    harvest()


Este código solo llama a harvest() cuando can_harvest() es True. 
Tiene el mismo efecto que

while True:
	if can_harvest():
		harvest()


En bucles anidados, continue siempre afecta al bucle más interno.

for i in range(10):
	for j in range(10):
	    print("this is printed 100 times")
		continue
		print("this is never printed")
	print("this is printed 10 times")


## Diccionarios
Los diccionarios son una estructura de datos que te permite mapear claves a valores de la misma manera que un diccionario real mapea palabras a sus definiciones y puedes buscarlas muy rápidamente.

Un diccionario se puede crear así:

right_of = {North:East, East:South, South:West, West:North}


La expresión antes de los dos puntos es la clave y la expresión después de los dos puntos es el valor al que se mapea la clave.
El diccionario anterior mapea cada dirección a la dirección a su derecha.

Aquí hay otro que mapea la posición del dron a la entidad sobre la que se encuentra.

x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}


Acceder al valor mapeado a una clave es similar a acceder a un elemento en una lista:
value = dict[key]

Ejemplo:
orientation = right_of[South]
Esto establece orientation en West.

Puedes añadir un nuevo par clave-valor a un diccionario así:
dict[key] = value

Ejemplo:
entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
Esto actualiza la entidad almacenada para la posición actual.

Las claves son únicas, por lo que añadir una clave que ya existe en el diccionario sobrescribirá el valor anterior.

Usa dict.pop(key) para eliminar un par clave-valor de dict.

key in dict evalúa a True si key es una clave en el dict y False en caso contrario.
Así que puedes usar if key in dict: para comprobar si dict contiene la clave.

Poner un diccionario en un bucle for te permite iterar a través de todas las claves:
for key in dict:
	value = dict[key]

No hay garantías sobre el orden en que se iteran las claves.

Ver también [Conjuntos](#conjuntos)

## Bucle For
El bucle for funciona como en Python. (Llamado bucle foreach en algunos lenguajes, no confundir con el bucle for de estilo C, que es algo diferente).

for i in sequence:
	#hacer algo con i

Similar al bucle while, el bucle for también llama repetidamente a un bloque de código. En lugar de iterar basándose en una condición, ejecuta el cuerpo del bucle una vez por cada elemento en una secuencia.

**Sintaxis**

Un bucle for se ve así:

for variable_name in sequence:
	#bloque de código

variable_name puede ser cualquier nombre que elijas. Es una variable que almacena el elemento actual en la secuencia. sequence necesita ser algún valor que se pueda iterar, como un rango de números. El bloque de código se ejecuta para cada elemento con la variable del bucle asignada a ese elemento.

**Secuencias**

[Rangos](#rangos) [Listas](#listas) [Tuplas](#tuplas) [Diccionarios](#diccionarios) [Conjuntos](#conjuntos)

**Ejemplo**

for i in range(5):
    harvest()

Este bucle ejecuta el cuerpo un número fijo de veces. Es esencialmente lo mismo que escribir

i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()

Así que llama a harvest() 5 veces.

Ver también [Break](#break)  y [Continue](#continue)

## Funciones
Usa la palabra clave def para definir una nueva función:
def f(arg1, arg2 = False):
	#código de la función

Puedes usar el operador de llamada () para llamar a la función:
f(42)

Consulta también [Ambitos](#ambitos-de-nombres) para aprender sobre variables locales y globales en funciones.

**Introducción**
Ya has visto funciones integradas como harvest().
También puedes definir tus propias funciones, lo que te permite estructurar tu código de forma modular. Básicamente, te permite dar un nombre a un bloque de código para que puedas llamarlo desde donde quieras.

**Definiciones de Funciones**
Por ejemplo, podrías definir una función que mueva el dron varias veces.

def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

La palabra clave def indica que esto es una definición de función. 
move_n_dir es el nombre al que se vincula la función. Puede ser cualquier nombre de variable válido y se usará para llamar a la función.
n y dir son parámetros. Son variables que contienen los valores que se pasan a la función (estos valores también se llaman argumentos). Puedes añadir tantos parámetros como quieras a la definición de una función.
Después de los : viene el bloque de código que se ejecutará cuando se llame a la función.

Con la definición anterior, el siguiente código mueve el dron 10 casillas hacia el North y 2 casillas hacia el West.

move_n_dir(10, North)
move_n_dir(2, West)

Cuando veas def function():, deberías pensar en ello como una asignación de variable como esta:
function = create_new_function_object()
Como con todas las asignaciones, ¡no puedes usar la variable antes de que se le haya asignado un valor!
La instrucción def debe ejecutarse antes de cualquier llamada a la función.
Este código lanzará un error:

func()
def func():
	pass

**Valores de Retorno**
Usa la palabra clave return para hacer que una función devuelva un valor. 
Por ejemplo, la siguiente función define la operación "o exclusivo". El "o exclusivo" devuelve True si un valor es True y el otro es False:

def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()

Las [Tuplas](#tuplas) permiten devolver múltiples valores.

**Argumentos por Defecto**
También puedes asignar valores por defecto que se usarán si no se pasan argumentos.

def f(a = False):
	if a:
		do_a_flip()

f()

f(True)

Un argumento que tiene un valor por defecto no puede ser seguido por un argumento que no tiene un valor por defecto.

**Uso Avanzado de Funciones**
Las funciones son valores como cualquier otro, y la instrucción def actúa como una instrucción de asignación, asignando la función al nombre que le des.
Esto permite hacer cosas como esta:

def f():
	def d():
		do_a_flip()
	return d

f()()

Aquí f() llama a la función f, que define y devuelve una nueva función d. El segundo () ejecuta la función devuelta y realiza un giro.
(Hacer este tipo de cosas no suele ser una buena idea porque es difícil ver lo que está pasando)

Las funciones que toman otras funciones como argumentos te permiten ser muy creativo:

def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)

Este código mueve el dron hacia el North 10 veces y luego usa fertilizante 10 veces.


## If
Puedes usar if, elif y else para ejecutar código condicionalmente.

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()

**Sintaxis**
Los if te permiten ejecutar código solo si una condición es True. Son como un bucle while que no se repite.
El if toma una condición igual que el bucle while y ejecuta el bloque de código del if si la condición evalúa a True:

#hacer un giro si la condición es True
if condition:
	do_a_flip()

También puedes añadir un else después del if que define el código a ejecutar si la condición evalúa a False.

Haz un giro si la condition es True, de lo contrario, cosecha.
if condition:
	do_a_flip()
else:
	harvest()

elif es la abreviatura de else if.

if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c

se puede acortar a:

if condition1:
	#a
elif condition2:
	#b
else:
	#c

## Import
Poner todo tu código en un solo archivo se vuelve inmanejable rápidamente. 
Las sentencias import te permiten importar funciones y variables globales de otro archivo.
Cómo funciona en una captura de pantalla:

screen module1
import module2
module2.x += 1
module2.print_x()

screen module2
x = 0
def print_x():
    print(x)

print 1

Aquí, import module2 ejecuta el archivo llamado module2 y te da acceso a todas sus variables globales.
Luego puedes acceder a las variables y funciones dentro del módulo importado usando el operador ..
Así que en este ejemplo, module2.print_x() llama a print_x() en module2.

También puedes mover las variables globales del módulo importado al ámbito actual donde se ejecuta la sentencia de importación usando la sintaxis from.

from module2 import print_x
print_x()
Importa solo las variables globales especificadas de module2.

o

from module2 import *
print_x()
Importa todas las variables globales de module2.

Esto también importa el archivo module2, pero en lugar de acceder a él a través de una variable llamada module2, desempaqueta las variables globales de module2 y las asigna directamente en el ámbito local.

Esta forma de importar no suele recomendarse porque no funciona bien cuando dos archivos se importan mutuamente, y podrías sobrescribir accidentalmente variables en el archivo que importa debido a colisiones de nombres. Es más seguro evitar la sintaxis from si no sabes lo que estás haciendo.

**Cómo funciona realmente**
**En resumen**
Las importaciones pueden ser poco intuitivas, pero la mayoría de los problemas se pueden evitar usando la sintaxis import archivo en lugar de from archivo import, y envolviendo todo lo que no sea una definición global en
if __name__ == "__main__":

**Efectos Secundarios de la Importación**
La primera vez que importas un archivo, se ejecutará el archivo completo y luego te dará acceso a todas las variables que se hayan definido durante la ejecución.
Si importas el mismo archivo de nuevo, simplemente devolverá el módulo guardado en caché de la primera vez.

Esto significa que las sentencias de importación pueden tener efectos secundarios. Si importas un archivo que llama a harvest(), realmente cosechará durante la importación. Pero cuando lo importes de nuevo, no volverá a cosechar porque el archivo solo se ejecuta una vez.

Hay una forma de evitar tales efectos secundarios usando la variable __name__. Esta es una variable que se establece automáticamente a "__main__" cuando un archivo se ejecuta directamente, y al nombre del archivo cuando se ejecuta a través de import.
Se considera una buena práctica poner cualquier código que no quieras que se ejecute cuando se importa el archivo dentro de un bloque if __name__ == "__main__":.

Una estructura de archivo común en Python es poner el código que debe ejecutarse cuando se ejecuta el archivo en una función main(). De esta manera tienes una distinción clara entre las variables locales (definidas dentro de main()) y las variables globales que se pueden importar (definidas fuera de main()).

una_variable_global = "global"

def main():
    una_variable_local = "local"
    # hacer cosas

if __name__ == "__main__":
    main()

**Ciclos de Importación**
¿Qué pasa si el archivo a importa el archivo b y el archivo b importa el archivo a?

archivo a:
import b
x = 0

archivo b:
import a
def f():
    print(a.x)

Esto funcionará bien. Digamos que ninguno de los dos archivos está cargado todavía, y alguien más ejecuta import a.

-a se ejecuta hasta la línea import b.
-b se ejecuta hasta la línea import a.
-El módulo a ya existe, pero no contiene x porque solo ha llegado hasta la línea import b.
-b guarda una referencia al módulo a a medio cargar en una variable llamada a.
-b ejecuta la sentencia def y guarda la función f().
-a continúa ejecutándose e inicializa x.

Cuando alguien llama a b.f(), imprimirá 0 correctamente porque el módulo a al que b tiene una referencia ya está completamente cargado.

Ahora considera el mismo código usando la sintaxis from.

archivo a:
from b import *
x = 0

archivo b:
from a import *
def f():
    print(x)

-a se ejecuta hasta la línea from b import *.
-b se ejecuta hasta la línea from a import *.
-El módulo a ya existe, pero aún no se ha ejecutado completamente.
-b desempaqueta todo lo que está actualmente en a en su propio ámbito global. En este punto, a no contiene nada porque aún no ha llegado a la línea x = 0, por lo que no se importa nada.
-b ejecuta la sentencia def y guarda la función f().
-a continúa ejecutándose e inicializa x.

Si alguien llama ahora a b.f(), obtendrá un error de que x no existe en el ámbito actual. Esto se debe a que esta vez b no tiene una referencia a a que todavía se está cargando y no ve las definiciones que se añadieron después de la importación.

## Listas
Las listas son una forma fácil de almacenar múltiples valores en una sola variable.
Puedes crear nuevas listas así:

some_list = [2, True, Items.Hay]

La lista ahora contiene los valores 2, True y Items.Hay.
Una lista también puede estar vacía:

empty_list = []

Puedes acceder a un elemento de una lista por su índice. El índice es 0 para el primer elemento, 1 para el segundo, 2 para el tercero...

planta zanahorias
entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])

Puedes iterar sobre una lista usando un bucle for. El siguiente ejemplo suma todos los elementos de la lista.

numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number
sum ahora es 18

Los siguientes métodos de lista te permiten añadir y eliminar elementos:

elements.append(elem) añade un elemento al final de la lista:

numbers = [2, 6, 12]
numbers.append(7)
numbers ahora es [2, 6, 12, 7]

elements.remove(elem) elimina la primera aparición de un elemento de una lista:

numbers = [1, 2, 4, 2]
numbers.remove(2)
numbers ahora es [1, 4, 2]

elements.insert(index, elem) inserta un elemento en el índice dado:

some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)
some_list ahora es [Entities.Tree, Items.Wood, Items.Hay]

elements.pop(index) elimina el elemento en el índice especificado.
Si no se especifica ningún índice, se elimina el último ítem.

numbers = [3, 5, 8, 25]
numbers.pop()
numbers ahora es [3, 5, 8]
numbers.pop(1)
numbers ahora es [3, 8]

La función len() devuelve la longitud de la lista.
numbers = [3, 2, 1]
x = len(numbers)
x ahora es 3

Las listas tienen semántica de referencia. Esto significa que asignar una lista a una variable le asigna el mismo objeto de lista, en lugar de hacer una copia de la lista.
Si dos variables hacen referencia a la misma lista, los cambios en la lista serán visibles para ambas.

a = [1, 2]
b = a
b.pop()
a y b ahora son ambos [1]


## Operadores
operadores aritméticos: +, -, *, /, //, %, **
operadores de comparación: ==, !=, <=, >=, <, >
operadores booleanos: not, and, or

Nota: Todos los números en el juego son números de punto flotante. Así que todos los operadores aritméticos son operadores de punto flotante.
// se define para redondear hacia abajo el número después de la división.

Para los operadores de asignación necesitas desbloquear la mejora "Variables".

**Introducción**
Los operadores te permiten comparar, modificar y combinar valores. 
Los operadores aritméticos +, -, *, /, //, %, ** se usan para realizar operaciones matemáticas comunes con números. 
Los operadores de comparación ==, !=, <=, >=, <, > se usan para comparar valores. El resultado siempre es True o False.
Los operadores lógicos (también llamados operadores booleanos) not, and, or se usan para combinar valores de verdad.

**Operadores Aritméticos**
Los signos + y - se usan para la suma y la resta.

2 + 3 evalúa a 5
3 - 2 evalúa a 1

*, / y // se usan para la multiplicación y la división.

2 * 3 evalúa a 6
5 / 2 evalúa a 2.5

// hace lo mismo que / pero el resultado se redondea hacia abajo (al siguiente entero).

5 // 2 evalúa a 2

% es el operador de módulo, también conocido como el operador de resto. Esencialmente, divide los dos números y luego devuelve el resto. También puedes pensar en ello como restar repetidamente el número de la derecha del número de la izquierda hasta que el resto sea menor que el número de la derecha.

4 % 2 evalúa a 0
5 % 2 evalúa a 1
6 % 2 evalúa a 0
2 % 6 evalúa a 2
1.5 % 1 evalúa a 0.5

** es el operador de potencia.

2**2 evalúa a 4
(-5)**3 evalúa a -125

**Operadores de Comparación**
== y != se usan para comprobar si dos valores son "iguales"(==) o "no iguales"(!=). Se pueden usar en todo tipo de valores.

2 == 2 evalúa a True
Entities.Bush != Entities.Bush evalúa a False
3 != 3 + 1 evalúa a True

<=, >=, <, > solo se pueden usar en números. Comprueban si el número de la izquierda es "menor o igual"(<=), "mayor o igual"(>=), "menor" (<) o "mayor" (>) que el número de la derecha.

1 <= 1 evalúa a True
2 >= 3 evalúa a False
-2 < -1 evalúa a True
6 > 6 evalúa a False

**Operadores Lógicos**
not simplemente invierte el valor:

not False evalúa a True
not True evalúa a False

and evalúa a True solo si ambos valores son True

True and True evalúa a True
True and False evalúa a False
False and False evalúa a False

or evalúa a True si al menos uno de los valores es True

True or True evalúa a True
True or False evalúa a True
False or False evalúa a False

## Ambitos de Nombres
Los ámbitos determinan qué variables se pueden acceder y desde dónde. Un ámbito es básicamente una correspondencia de nombres a valores.
Funcionan básicamente igual que en Python.

Hay un ámbito global, y cada función tiene un ámbito local.
Cuando defines una variable, se añade al ámbito actual.
Cualquier cosa fuera de la definición de una función se considera parte del ámbito global.

x = 1
Asigna un valor de 1 al nombre x en el ámbito global.

Esta instrucción def asigna una función al nombre f en el ámbito global.
def f():
    Asigna un valor de 1 al nombre y en el ámbito local de f.
    y = 1

    Asigna una función al nombre g en el ámbito local de f.
    def g():
        pass

f()
Recupera la función almacenada en f del ámbito global y la llama.

print(y)
Esta instrucción print en el ámbito global lanza un error porque y nunca se declaró en el ámbito global, así que no podemos leerlo aquí.
Solo existía en el ámbito local de f.

**La palabra clave global**
Por defecto, todas las variables en las funciones se vinculan al ámbito local, incluso si existe una variable con el mismo nombre en el ámbito global.

x = 0

def f():
    x = 1
f()
print(x)

Este código imprime 0 porque la x local dentro de f no es la misma variable que la x global, por lo que la x global permanece sin cambios. Esto es importante porque, de lo contrario, una llamada a función podría sobrescribir accidentalmente una variable global que simplemente tiene el mismo nombre que una variable local de esa función.

Si quieres escribir en una variable global, debes hacerlo explícitamente usando la palabra clave global.

x = 0

def f():
    global x
    x = 1
f()
print(x)

En este ejemplo, global x vincula x a la variable global x definida encima de ella. Esto ahora imprimirá 1.
Ten en cuenta que cambiar variables globales suele ser el primer paso hacia el código espagueti, donde cada parte del programa afecta a todas las demás, así que no abuses de ello.

**Bucles y Ramificaciones**
Los bucles y las ramificaciones no crean sus propios ámbitos, por lo que cualquier cosa declarada dentro de ellos todavía se puede usar fuera.

for i in range(3):
    pass
print(i)

Esto imprimirá 2 porque la última iteración del bucle for asignó 2 a i.

## Conjuntos
Los conjuntos son como los [diccionarios](#diccionarios), pero sin valores. Son solo un conjunto desordenado de claves. 

Se crean como los diccionarios, pero sin valores.
set = {North, East, West}

Usa set() para crear un conjunto vacío. Ten en cuenta que {} crea un diccionario vacío.

Usa set.add(elem) para añadir un nuevo elemento al conjunto.

Usa set.remove(elem) para eliminar un elemento de un conjunto.

Usa if elem in set: para comprobar si el conjunto contiene un elemento.

Usa for elem in set: para iterar sobre todos los elementos del conjunto.
Para conjuntos más grandes, el operador in funciona mucho más rápido que en una lista.

Al igual que los diccionarios, los conjuntos son desordenados, por lo que no hay garantías sobre el orden en que se iteran los elementos.

Además, los elementos en los conjuntos son únicos, por lo que añadir un elemento que ya está en el conjunto no cambiará el conjunto.

## Tuplas
Las tuplas son una excelente manera de combinar múltiples valores en un solo valor.
Para crear una tupla, simplemente separa los valores con comas:

tuple = 1, 2

También puedes desempaquetarlas en varias variables de nuevo. En el código de abajo, la tupla (1,2) se desempaqueta en dos variables a y b.

a, b = 1, 2

Las tuplas se pueden indexar como las listas, pero son inmutables y no se pueden cambiar después de su creación.

tuple = 1, 2

print(tuple[1])
imprime 2

tuple[0] = 3
lanza un error

A diferencia de las listas, las tuplas se pueden usar como claves en los diccionarios.

d = {(1,2):(4,5)}

print(d[(1,2)])
imprime (4,5)

También pueden ser útiles para devolver múltiples valores en una función.

def f():
    return 1, 2

a, b = f()

## Variables
Las variables se pueden considerar como contenedores con nombre que pueden almacenar un valor.
El operador = se usa para declarar una variable y almacenar un valor en ella.

nombre_variable = valor

El lado izquierdo del operador es el nombre de la variable. Puedes darle el nombre que quieras.
El lado derecho es una expresión cuyo valor resultante se almacenará en la variable.

Declara una variable llamada a y almacena el valor 5 en ella:
a = 5
Declara una variable llamada b y almacena el valor de retorno de can_harvest() en ella:
b = can_harvest()

No confundas el operador = con el operador ==. 
El operador == comprueba si dos valores son iguales y devuelve True o False.
El operador = asigna el valor de la derecha al nombre de la izquierda.

Después de que se ha asignado una variable, puedes usarla en el código para recuperar el valor que contiene

a = 5
for i in range(a):
	do_a_flip()

El bucle anterior se ejecuta 5 veces porque a está establecido en 5.
La i en el bucle for también es una variable a la que se le asigna automáticamente el valor actual de la secuencia en cada iteración del bucle. (No tiene que llamarse i, puedes darle cualquier nombre de variable válido).

Las variables también te permiten hacer lo mismo con un bucle while:

a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1

Esto hace lo mismo que el bucle for de arriba. Solo tenemos que incrementar i manualmente.
Ten en cuenta que para incrementar i, lo establecemos a su propio valor más 1. Cambiar el valor de una variable basándose en su valor anterior es algo muy común. 
Se puede abreviar usando estos operadores: +=, -=, *=, /=, %=

i = i + 1 es lo mismo que i += 1
a = a / 3 es lo mismo que a /= 3

## Bucle While
Has desbloqueado el bucle while y los valores True y False. El bucle while sigue ejecutando el cuerpo del bucle mientras la condición sea True.

while condition:
	#cuerpo del bucle

No te preocupes por crear bucles infinitos. Los retrasos en la ejecución evitarán que el programa se congele.

**Para Principiantes**
Quizás ya has intentado poner varias llamadas a harvest() seguidas:

harvest()
harvest()
harvest()

Esto te permite cosechar varias veces en una sola ejecución del programa. 
Sin embargo, sería bueno cosechar más de tres veces, y escribir el mismo código varias veces es una mala práctica. 
La solución es un bucle. 
Un bucle te permite ejecutar el mismo código varias veces.

El bucle while toma una condición, que es un valor lógico que solo puede estar en uno de dos estados: True o False. 
Tal valor se llama valor booleano.

El bucle luego ejecuta el código dentro del bucle hasta que la condición sea False.
El bucle while se ve así:

while condition:
	#cuerpo del bucle
	#cuerpo del bucle
	#...
	
Donde tienes que reemplazar "condition" por un valor booleano y #cuerpo del bucle por lo que quieras hacer en el bucle.

Hay dos valores booleanos constantes disponibles. Las constantes son valores que nunca cambian durante el programa.

Para crear un valor booleano constante que siempre sea True, simplemente puedes escribir True. Escribe False como un valor booleano constante que siempre será False.
Así que podrías escribir


while False:
	do_a_flip()

o

while True:
	do_a_flip()

El primero nunca hará un giro y el segundo hará giros para siempre (un bucle infinito). 

Normalmente, crear un bucle infinito es una mala idea porque congelará el programa, pero en este juego hay retrasos entre cada iteración del bucle, por lo que hará que el dron siga haciendo giros hasta que lo detengas manualmente presionando de nuevo el botón de ejecutar.

Observa cómo la línea después de los dos puntos está indentada. La indentación como esta se usa para separar bloques de código.
Simplemente presiona Tab para añadir indentación y Shift + Tab (o Retroceso) para quitarla.

El bucle repetirá todas las instrucciones indentadas después de los dos puntos.
Las instrucciones después del bloque indentado se ejecutarán después de que el bucle haya terminado.


# Desbloqueos

## Cactus
Como otras plantas, los [cactus](#cactus-1) pueden cultivarse en tierra y cosecharse como de costumbre.

Sin embargo, vienen en varios tamaños y tienen un extraño sentido del orden.

Si cosechas un cactus completamente crecido y todos los cactus vecinos están en orden, también cosechará todos los cactus vecinos de forma recursiva.

Un cactus se considera ordenado si todos los cactus vecinos al North y East están completamente crecidos y son de tamaño mayor o igual, y todos los cactus vecinos al South y West están completamente crecidos y son de tamaño menor o igual.

La cosecha solo se propagará si todos los cactus adyacentes están completamente crecidos y en orden.
Esto significa que si un cuadrado de cactus crecidos está ordenado por tamaño y cosechas un cactus, se cosechará todo el cuadrado.

Un cactus completamente crecido aparecerá marrón si no está ordenado. Una vez ordenado, se volverá verde de nuevo.

Recibirás una cantidad de cactus igual al número de cactus cosechados al cuadrado. Así que si cosechas n cactus simultáneamente, recibirás n**2 Items.Cactus.

El tamaño de un cactus se puede medir con measure().
Siempre es uno de estos números: 0,1,2,3,4,5,6,7,8,9.

También puedes pasar una dirección a measure(direction) para medir la casilla vecina en esa dirección del dron.

Puedes intercambiar un cactus con su vecino en cualquier dirección usando el comando swap().
swap(direction) intercambia el objeto debajo del dron con el objeto a una casilla de distancia en la direction del dron.

**Ejemplos**

En cada una de estas cuadrículas, todos los cactus están ordenados y la cosecha se extenderá por todo el campo:
3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4

En esta cuadrícula, solo el cactus inferior izquierdo está ordenado, lo que no es suficiente para que se propague:
1 5 3
4 9 7
3 3 2

Si las filas ya están ordenadas, ordenar las columnas no desordenará las filas.
Si no estás familiarizado con los algoritmos de ordenamiento, quizás quieras buscarlos en línea y pensar cuáles podrían adaptarse a este problema. Ten en cuenta que no todos funcionan porque solo puedes intercambiar cactus vecinos.

## Zanahorias
Antes de poder plantar zanahorias con plant(Entities.Carrot), tienes que arar la tierra. Esto cambiará el terreno a Grounds.Soil. Para arar la tierra, simplemente llama a till(). Llamar a till() de nuevo lo cambiará de vuelta a Grounds.Grassland.

Plantar zanahorias cuesta madera y heno. Estos ítems se eliminarán automáticamente al llamar a plant(Entities.Carrot).

Puedes ver el coste de cualquier planta en su [propia página](#carrot)

## Depuración
[Depuración](#depuración)

## Depuración 2
Cuando tu dron se vuelve demasiado rápido y la cuadrícula demasiado grande, puede ser difícil ver lo que está pasando.

Por esta razón existen las funciones set_execution_speed() y set_world_size().
Te permiten reducir la velocidad de ejecución y el tamaño de la granja. 

El tamaño de la granja y la velocidad de ejecución se restablecerán a los valores predeterminados al final de la ejecución.

## Diccionarios
[Diccionarios](#diccionarios)

## Expansión 1
Consulta también [Expansión_2](#expansión-2)

¡Tu granja ha crecido! Este espacio no es de mucha utilidad si no puedes mover el dron, así que hay una nueva función move() que mueve el dron. move() requiere que especifiques la dirección en la que quieres que se mueva el dron. Hay cuatro nuevas constantes para esto: North, East, South, West

Por ejemplo, move(North) moverá el dron una casilla hacia el norte.

Si te mueves por el borde de la granja, el dron será movido al otro lado de la granja.
El siguiente código de ejemplo seguirá moviendo el dron hacia el norte y volverá al principio cuando llegue al borde de la granja:

while True:
	move(North)

## Expansión 2
¡Tu granja se ha expandido de nuevo! Ahora las casillas ya no están en una bonita fila, así que necesitas encontrar una manera de recorrer una cuadrícula cuadrada.

Con el bucle while esto no es posible hasta que desbloquees los sentidos y los operadores.
Es hora de introducir el bucle for.

Puedes leer todo sobre el bucle for en la página [Bucle For](#bucle-for), pero por ahora solo lo necesitarás para repetir código un número fijo de veces.

#hacer n giros
for i in range(5):
	do_a_flip()

range(n) crea un rango de números de 0 a n-1 que tiene n elementos. El bucle for ejecuta su cuerpo una vez por cada elemento en la secuencia. En este ejemplo, do_a_flip() se llamará 5 veces.

La función get_world_size() también está disponible ahora. Devuelve la longitud del lado de tu granja. De esta manera, puedes escribir código que no se romperá con la próxima mejora de expansión.

for i in range(get_world_size()):
	harvest()
	move(North)

Este ejemplo cosecha una columna de la granja para cualquier tamaño de granja.

Si estás atascado tratando de averiguar cómo mover el dron por la granja, consulta la pista de abajo.

Hay, por supuesto, varias formas de moverse por la granja.
Lo que buscamos es una forma de recorrerla de manera sistemática que no se rompa cuando la granja vuelva a crecer.
Una forma sistemática de llegar a todos los lugares de la granja sería repetir los siguientes 2 pasos para siempre:

1.Moverse hacia el North hasta que vuelva al principio.
2.Moverse hacia el East

for i in range(get_world_size()): puede ser útil para convertir esta idea en código.

El recorrido básico podría ser así:

for i in range(get_world_size()):
	for j in range(get_world_size()):
		#hacer un giro en cada casilla
		do_a_flip()
		move(North)
	move(East)

## Fertilizante
En algún momento, esperar a que las plantas crezcan ya no es lo suficientemente eficiente. 
Similar al agua, recibirás automáticamente 1 fertilizante cada 10 segundos, y uno más con cada mejora.

El fertilizante puede hacer que las plantas crezcan instantáneamente. use_item(Items.Fertilizer) reduce el tiempo de crecimiento restante de la planta bajo el dron en 2 segundos.

Esto tiene algunos efectos secundarios.
Las plantas cultivadas con fertilizante se infectarán.

Cuando una planta está infectada, la mitad de su rendimiento se convierte en Items.Weird_Substance cuando se cosecha.
La Sustancia Rara también se puede usar en las plantas, lo que tiene el efecto de cambiar el estado de infección de la planta y de todas las plantas adyacentes.

Así que si llamas a use_item(Items.Weird_Substance) en una planta infectada, la curará, pero si la usas en una planta sana, la infectará.

Si la usas en una planta infectada que tiene vecinos sanos, curará la planta pero infectará a los vecinos y viceversa.



## Funciones
[Funciones](#funciones)

## Hierba
Aumenta el rendimiento de la hierba.
51200%

## Sombreros
Has desbloqueado algunos colores nuevos de sombrero para tu dron.

Equípalos así:
change_hat(Hats.Gray_Hat)
do_a_flip()
change_hat(Hats.Purple_Hat)
do_a_flip()
change_hat(Hats.Green_Hat)
do_a_flip()
change_hat(Hats.Brown_Hat)
do_a_flip()

## Import
[Import](#import)

## Listas
[Listas](#listas)

## Bucle While
[Bucle While](#bucle-while)

## Laberintos
Items.Weird_Substance, que se obtiene [fertilizando](#fertilizante) plantas, tiene un efecto extraño en los arbustos. Si el dron está sobre un arbusto y llamas a use_item(Items.Weird_Substance, amount), el arbusto se convertirá en un laberinto de setos.
El tamaño del laberinto depende de la cantidad de Items.Weird_Substance utilizada (el segundo argumento de la llamada a use_item()).
Sin mejoras de laberinto, usar n Items.Weird_Substance resultará en un laberinto de nxn. Cada nivel de mejora del laberinto duplica el tesoro, pero también duplica la cantidad de Items.Weird_Substance necesaria. 
Así que para hacer un laberinto de campo completo:

plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)


Por alguna razón, el dron no puede volar sobre los setos, aunque no parezcan tan altos.

Hay un tesoro escondido en algún lugar del seto. Usa harvest() en el tesoro para recibir oro igual al área del laberinto. (Por ejemplo, un laberinto de 5x5 producirá 25 de oro).

Si usas harvest() en cualquier otro lugar, el laberinto simplemente desaparecerá.

get_entity_type() es igual a Entities.Treasure si el dron está sobre el tesoro y Entities.Hedge en cualquier otro lugar del laberinto.

Los laberintos no contienen bucles a menos que reutilices el laberinto (ver más abajo cómo reutilizar un laberinto). Así que no hay forma de que el dron termine en la misma posición de nuevo sin retroceder.

Puedes comprobar si hay una pared intentando moverte a través de ella. 
move() devuelve True si tuvo éxito y False en caso contrario.

can_move() se puede usar para comprobar si hay una pared sin moverse.

Si no tienes idea de cómo llegar al tesoro, echa un vistazo a la Pista 1. Te muestra cómo abordar un problema como este.

Usar measure() en cualquier lugar del laberinto devuelve la posición del tesoro.
x, y = measure()

Para un desafío extra, también puedes reutilizar el laberinto usando la misma cantidad de Items.Weird_Substance en el tesoro de nuevo. 
Esto recogerá el tesoro y generará un nuevo tesoro en una posición aleatoria del laberinto.

Cada vez que se mueve el tesoro, se pueden eliminar algunas de las paredes del laberinto de forma aleatoria. Así que los laberintos reutilizados pueden contener bucles.

Ten en cuenta que los bucles en el laberinto lo hacen mucho más difícil porque significa que puedes llegar a la misma ubicación de nuevo sin retroceder.
Reutilizar un laberinto no te da más oro que simplemente cosechar y generar un nuevo laberinto.
Este es un desafío 100% extra que puedes omitir.
Solo vale la pena si la información extra y los atajos te ayudan a resolver el laberinto más rápido.

El tesoro se puede reubicar hasta 300 veces. Después de eso, usar sustancia rara en el tesoro ya no aumentará el oro en él y ya no se moverá más.

Aquí tienes un enfoque general para resolver el problema:

Crea un laberinto e imagina que eres el dron.

Piensa en cómo intentarías encontrar el tesoro si estuvieras en el laberinto.

Escribe tu estrategia paso a paso para que otra persona pueda seguirla sin pensar.

Ahora intenta traducir tus pasos a código.

Mientras no haya bucles: todas las paredes son en realidad una gran pared conectada. Si sigues la pared, te llevará por todo el laberinto.
Este enfoque requiere muy poco código y no necesitas llevar un registro de dónde has estado. Unas 10 líneas de código es todo lo que necesitas.

En lugar de mover el dron en direcciones absolutas como este u oeste, puede ser muy útil moverlo en direcciones relativas como "girar a la derecha" o "girar a la izquierda". Para hacer esto, necesitas llevar un registro de la dirección en la que se está moviendo el dron. El dron nunca rota realmente, pero aún puedes mantener una rotación "virtual" en el código.
El siguiente truco de índice es útil para esto:

directions = [North, East, South, West]
index = 0

Usa % 4 para permitirle rotar "alrededor del círculo", de modo que después de West vuelva a North.
#girar a la derecha
            index = (index + 1) % 4

#girar a la izquierda
index = (index - 1) % 4

move(directions[index])

Si no puedes resolverlo, siempre puedes facilitarte la vida y hacerlo de manera menos eficiente. 
Resolver un laberinto de 1x1 es trivial.

## Megagranja
Este desbloqueo increíblemente poderoso te da acceso a múltiples drones. 

Como antes, todavía comienzas con un solo dron. Los drones adicionales deben ser generados primero y desaparecerán después de que el programa termine.
Cada dron ejecuta su propio programa por separado. Se pueden generar nuevos drones usando la función spawn_drone(function).

def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)

Esto genera un nuevo dron en la misma posición que el dron que ejecutó el comando spawn_drone(function). El nuevo dron comienza a ejecutar la función especificada. Después de que termina, desaparecerá automáticamente.

Los drones no chocan entre sí. 

Usa max_drones() para obtener el número máximo de drones que pueden existir simultáneamente.
Usa num_drones() para obtener el número de drones que ya están en la granja.


**Ejemplo:**
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)

Esto hará que tu primer dron se mueva horizontalmente y genere más drones. Los drones generados se moverán verticalmente y cosecharán todo a su paso.

Si ya se han generado todos los drones disponibles, spawn_drone() no hará nada y devolverá None.

Aquí hay otro ejemplo que pasa una dirección diferente a cada dron.
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)

**Todos los Drones son Iguales**
No hay un dron "principal" especial. Todos los drones pueden generar otros drones, y todos cuentan para el límite de drones. Todos los drones desaparecen cuando terminan. Si el primer dron termina su programa antes de tiempo, otro dron se convertirá en aquel cuya ejecución se visualiza con el resaltado de código. Todos los drones pueden activar breakpoints, y cuando un dron activa un breakpoint, el resaltado de código cambia a ese dron.

Echa un vistazo a esta súper útil función paralela for_all, que toma cualquier función y la ejecuta en cada casilla de la granja. Utiliza todos los drones disponibles para hacerlo.

def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)

Un patrón particularmente útil es generar un dron si hay uno disponible y, de lo contrario, hacerlo tú mismo.

if not spawn_drone(task):
	task()

**Esperar a otro Dron**
Usa la función wait_for(drone) para esperar a que otro dron termine. Recibes el handle del drone cuando lo generas.
wait_for(drone) devuelve el valor de retorno de la función que el otro dron estaba ejecutando.

def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))

Ten en cuenta que generar drones lleva tiempo, así que no es una buena idea generar un nuevo dron para cada pequeña cosa.

Puedes usar has_finished(drone) para ver si el dron ya terminó sin tener que esperar.

**Sin Memoria Compartida**
Cada dron tiene su propia memoria y no puede leer o escribir directamente las variables globales de otro dron.

x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)

Esto imprimirá 0 porque el nuevo dron incrementó su propia copia de la x global, lo que no afecta a la x del primer dron.

**Pasar Argumentos**
spawn_drone acepta otros argumentos opcionales que se pasarán a la función llamada:

def harvest_spiral(radius):
    for i in range(0, radius, 2):
        for j in range(i):
            harvest()
            move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)

wait_for(spawn_drone(harvest_spiral, 6))

Ten en cuenta que la cláusula de "Sin Memoria Compartida" sigue aplicándose. Esto significa que la función llamada opera sobre una copia de los argumentos:

def modify(list):
	move(North)
	list.append('green')
	print(list) # imprime ['red', 'green']

l = ['red']
wait_for(spawn_drone(modify, l))
print(l) # imprime ['red']

**Condiciones de Carrera**
Múltiples drones pueden interactuar con la misma casilla de la granja al mismo tiempo. Si dos drones interactúan con la misma casilla durante el mismo tick, ambas interacciones ocurrirán, pero los resultados pueden diferir según el orden de las interacciones.

Por ejemplo, imagina que los drones 0 y 1 están ambos sobre el mismo árbol que está casi completamente crecido.
El dron 0 llama a
use_item(Items.Fertilizer)
El dron 1 llama a
harvest()

Si estas acciones ocurren al mismo tiempo, el árbol primero será fertilizado y luego cosechado. En ese caso, recibirás madera de él. Sin embargo, si el dron 1 es ligeramente más rápido, el árbol será cosechado antes de ser fertilizado, y no recibirás la madera.
Esto se llama una "condición de carrera". Es un problema común en la programación paralela, donde el resultado depende del orden en que se realizan las operaciones.

Aquí hay otra situación problemática que puede ocurrir cuando múltiples drones ejecutan el mismo código simultáneamente en la misma posición.
if get_water() < 0.5:
    use_item(Items.Water)

Si múltiples drones ejecutan esto simultáneamente, todos ejecutarán la primera línea, lo que los pondrá en el bloque if. Luego, todos usarán agua, desperdiciando mucha.
Para cuando un dron llega a la segunda línea, get_water() podría ya no ser menor que 0.5 porque otro dron ha regado la casilla mientras tanto.

## Operadores
[Operadores](#operadores)

## Plantar
La hierba es agradable porque crece automáticamente. Todas las demás plantas deben ser plantadas con la función plant(). La única planta que puedes plantar ahora mismo es un arbusto.
Puedes pasar el tipo de planta que quieres plantar a la función de esta manera:

plant(Entities.Bush)

Esto plantará un arbusto debajo del dron.

Llama a clear() para restablecer la granja a todo hierba y restablecer la posición del dron.

Parece que si cultivas más de un tipo de planta en la granja al mismo tiempo, a veces puedes obtener un mayor rendimiento. Necesitarás investigar el policultivo para aprender más.

## Policultivo
Puede que ya hayas notado que a veces las plantas rinden más cuando se plantan juntas.
La hierba, los arbustos, los árboles y las zanahorias rinden más cuando tienen el compañero de planta adecuado. La preferencia de compañero es diferente para cada planta individual y no se puede predecir. Afortunadamente, la preferencia de compañero de la planta debajo del dron se puede medir usando get_companion(). Devuelve una tupla donde el primer elemento es el tipo de planta que quiere como compañero y el segundo elemento es la posición donde quiere a su compañero.

plant_type, (x, y) = get_companion()

Por ejemplo, si plantas un arbusto y luego llamas a get_companion(), devolverá algo como (Entities.Carrot, (3, 5)). Esto significa que a este arbusto le gustaría tener zanahorias en la posición (3,5). Así que si plantas zanahorias en (3,5) y luego cosechas el arbusto, rendirá más madera. La etapa de crecimiento de la zanahoria no importa.

La preferencia de compañero de una planta puede ser Entities.Grass, Entities.Bush, Entities.Tree o Entities.Carrot. Cada planta elige esto al azar, pero siempre elegirá una planta diferente a sí misma. La posición también puede ser cualquier posición dentro de 3 movimientos de la planta, excepto la posición de la planta misma.

Si no hay una planta debajo del dron que tenga una preferencia de compañero, get_companion() devolverá None.

Antes de que se desbloquee el policultivo, el multiplicador de rendimiento es 5. Se duplica cada vez que lo mejoras.

## Calabazas
Las [calabazas](#pumpkin) crecen como las zanahorias en suelo arado. Plantarlas cuesta zanahorias.

Cuando todas las calabazas en un cuadrado están completamente crecidas, crecerán juntas para formar una calabaza gigante. Desafortunadamente, las calabazas tienen un 20% de probabilidad de morir una vez que están completamente crecidas, por lo que necesitarás replantar las muertas si quieres que se fusionen. 

Cuando una calabaza muere, deja atrás una calabaza muerta que no soltará nada al ser cosechada. Plantar una nueva planta en su lugar elimina automáticamente la calabaza muerta, por lo que no es necesario cosecharla. can_harvest() siempre devuelve False en calabazas muertas.

El rendimiento de una calabaza gigante depende del tamaño de la calabaza.

Una calabaza de 1x1 rinde 1*1*1 = 1 calabazas.
Una calabaza de 2x2 rinde 2*2*2 = 8 calabazas en lugar de 4.
Una calabaza de 3x3 rinde 3*3*3 = 27 calabazas en lugar de 9.
Una calabaza de 4x4 rinde 4*4*4 = 64 calabazas en lugar de 16.
Una calabaza de 5x5 rinde 5*5*5 = 125 calabazas en lugar de 25.
Una calabaza de nxn rinde n*n*6 calabazas para n >= 6.

Es una buena idea obtener calabazas de tamaño al menos 6x6 para obtener el multiplicador completo. 

Esto significa que incluso si plantas una calabaza en cada casilla de un cuadrado, una de las calabazas puede morir e impedir que crezca la mega calabaza.

## Sentidos
¡El dron puede ver ahora! 

Las funciones get_pos_x() y get_pos_y() devuelven la posición x e y actual del dron. En la posición inicial ambas son 0. La posición x aumenta en 1 por cada casilla hacia el East y la posición y aumenta en 1 por cada casilla hacia el North.

num_items(item) devuelve cuántos de un ítem tienes.
Por ejemplo, num_items(Items.Hay) devuelve cuánto heno tienes.

get_entity_type() y get_ground_type() devuelven el tipo de entidad o terreno que hay debajo del dron.

Haz un giro si estás sobre un arbusto:
if get_entity_type() == Entities.Bush:
	do_a_flip()

¡La palabra clave None también está desbloqueada ahora! None es un valor que representa que no hay valor.
Por ejemplo, una función que no tiene una instrucción return en realidad devolverá None.

get_entity_type() devuelve None si no hay ninguna entidad debajo del dron.


Si quieres saber cuántos de un desbloqueo en particular tienes, usa la función num_unlocked(unlock).

Por ejemplo, num_unlocked(Unlocks.Speed) devolverá el número de mejoras de velocidad que tienes.

num_unlocked(Unlocks.Senses) devolverá 1 si los sentidos están desbloqueados y 0 si no lo están.

También puedes usar num_unlocked() en Ítems, Entidades o Terrenos. Esto devolverá 1 si está desbloqueado, de lo contrario 0.

Ten cuidado, num_unlocked(Unlocks.Carrots) devolverá el número de veces que se ha desbloqueado/mejorado.
num_unlocked(Items.Carrot) solo devolverá 0 o 1. (Lo mismo para otras plantas)

## Mejora de Velocidad
La velocidad de ejecución se ha duplicado. El problema es que ahora el dron cosecha más rápido de lo que la hierba puede crecer, lo que resulta en que no haya cosecha en absoluto. Para solucionar esto, ahora se han desbloqueado las ramificaciones [if](#if) y la función [can_harvest](#can_harvest).

**Comprobando Antes de Cosechar**
Hasta ahora solo teníamos True y False como condiciones, lo que por supuesto no es muy útil con if. 

La nueva función can_harvest() proporciona una mejor condición. can_harvest() devuelve True si la planta debajo del dron se puede cosechar y False en caso contrario.

if can_harvest():
	#hacer algo

La razón por la que puedes usar esta función como condición de esta manera es porque devuelve un valor booleano.

Un valor de retorno significa esencialmente que después de que se ejecute la funcionalidad, la expresión de la llamada a la función se evalúa al valor devuelto.

Lo que sucede cuando el código anterior se ejecuta:
	-el if se ejecuta
	-se llama a can_harvest()
	-can_harvest() hace lo suyo
	-can_harvest() devuelve True o False
	-la instrucción ahora es if True: o if False:
	-el bloque de código solo se ejecuta si se puede cosechar

Ahora podemos usar if para evitar que el dron coseche demasiado pronto.

## Girasoles
Los [girasoles](#sunflower) recogen la energía del sol. Puedes cosechar esa energía. 

Plantarlos funciona exactamente igual que plantar zanahorias o calabazas. 

Cosechar un girasol crecido produce energía.
Si hay al menos 10 girasoles en la granja y cosechas el que tiene el mayor número de pétalos, ¡obtienes 8 veces más energía!
Si cosechas un girasol mientras hay otro girasol con más pétalos, el siguiente girasol que coseches también te dará solo la cantidad normal de energía (no el bonus de 8x).

measure() devuelve el número de pétalos del girasol debajo del dron.
Los girasoles tienen al menos 7 y como máximo 15 pétalos.
Ya se pueden medir antes de que estén completamente crecidos.

Varios girasoles pueden tener el mismo número de pétalos, por lo que también puede haber varios girasoles con el mayor número de pétalos. En este caso, no importa cuál de ellos coseches.

Mientras tengas energía, el dron la usará para funcionar el doble de rápido. 
Consume 1 de energía cada 30 acciones (como movimientos, cosechas, siembras...)
Ejecutar otras instrucciones de código también puede usar energía, pero mucho menos que las acciones del dron.

En general, todo lo que se acelera con las mejoras de velocidad también se acelera con la energía.
Cualquier cosa acelerada por la energía también usa energía proporcional al tiempo que tarda en ejecutarse, ignorando las mejoras de velocidad.

## Medición de Tiempo
Si de verdad quieres optimizar tus métodos, necesitas entender cómo se mide el tiempo en este juego. Este desbloqueo trata sobre eso.

**Nuevas Funciones**
Hay dos funciones útiles para medir cuánto tardan las cosas:

get_time() devuelve el tiempo en segundos desde el inicio del juego.

get_tick_count() devuelve el número de ticks realizados desde el inicio de la ejecución.

Estas dos funciones, así como quick_print(), son completamente gratuitas. Incluso la operación de llamada es gratuita para ellas.

**Detalles de Ejecución**
**Aviso**
Así no es como funciona el rendimiento en el mundo real. Estas son solo reglas creadas para este juego para tener un modelo de tiempo consistente y comprensible.
Probablemente solo te importe esto si quieres hiperoptimizar tu código.


La unidad básica de tiempo para la ejecución de código se llama "tick". Sin mejoras de velocidad y energía, la ejecución procede a una velocidad de 400 ticks por segundo.

En general, las operaciones que combinan dos valores como +, -, *, /, //, %, and, or, ... tardan un tick en ejecutarse.
Los operadores unarios - y not son gratuitos.
Una ramificación if también tarda un tick en ejecutarse (además del tiempo que tarda en evaluar la expresión de la condición).
Las llamadas a funciones y las lecturas y escrituras de variables son gratuitas, pero las definiciones de funciones tardan 1 tick.
Las instrucciones import son gratuitas.
Acceder a un módulo importado con el operador . es gratuito.
Si una función o módulo se ha pasado a través de argumentos o asignaciones de variables, usarlo costará 1 tick en lugar de 0.
Los bucles for y while tardan un tick en empezar, pero las iteraciones son gratuitas (sin contar el tiempo para evaluar las expresiones de condición/secuencia).
return, break y continue son todos gratuitos.
pass tarda un tick, por lo que se puede usar para crear retrasos precisos.
Indexar en una estructura de datos tarda un tick para el operador de índice y, en el caso de un diccionario o conjunto, ticks adicionales dependiendo del tamaño de la clave.

El número de ticks que tardan en ejecutarse las funciones integradas está documentado en la documentación de cada función de forma individual.

## Arboles
Los [arboles](#tree) son una mejor manera de conseguir madera que los arbustos. Dan 5 de madera cada uno. Al igual que los arbustos, se pueden plantar en hierba o tierra.

A los árboles les gusta tener algo de espacio y plantarlos uno al lado del otro ralentizará su crecimiento. El tiempo de crecimiento se duplica por cada árbol que esté en una casilla directamente al norte, este, oeste o sur de él.

Así que si plantas árboles en cada casilla, tardarán 2*2*2*2 = 16 veces más en crecer.

El operador % puede ser útil aquí. Recuerda que el operador % devuelve el resto de la división. Los números pares divididos por 2 tienen un resto de 0 y los números impares divididos por 2 tienen un resto de 1.
Así que puedes comprobar si un número es par de esta manera:

def is_even(n):
	return n % 2 == 0

Esto devuelve True si n es par y False si no lo es.

## Variables
Las variables se pueden considerar como contenedores con nombre que pueden almacenar un valor.
El operador = se usa para declarar una variable y almacenar un valor en ella.

nombre_variable = valor

El lado izquierdo del operador es el nombre de la variable. Puedes darle el nombre que quieras.
El lado derecho es una expresión cuyo valor resultante se almacenará en la variable.

Declara una variable llamada a y almacena el valor 5 en ella:
a = 5
Declara una variable llamada b y almacena el valor de retorno de can_harvest() en ella:
b = can_harvest()

No confundas el operador = con el operador ==. 
El operador == comprueba si dos valores son iguales y devuelve True o False.
El operador = asigna el valor de la derecha al nombre de la izquierda.

Después de que se ha asignado una variable, puedes usarla en el código para recuperar el valor que contiene

a = 5
for i in range(a):
	do_a_flip()

El bucle anterior se ejecuta 5 veces porque a está establecido en 5.
La i en el bucle for también es una variable a la que se le asigna automáticamente el valor actual de la secuencia en cada iteración del bucle. (No tiene que llamarse i, puedes darle cualquier nombre de variable válido).

Las variables también te permiten hacer lo mismo con un bucle while:

a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1

Esto hace lo mismo que el bucle for de arriba. Solo tenemos que incrementar i manualmente.
Ten en cuenta que para incrementar i, lo establecemos a su propio valor más 1. Cambiar el valor de una variable basándose en su valor anterior es algo muy común. 
Se puede abreviar usando estos operadores: +=, -=, *=, /=, %=

i = i + 1 es lo mismo que i += 1
a = a / 3 es lo mismo que a /= 3

## Riego
Las plantas crecen más rápido cuando se riegan. El suelo tiene un nivel de agua que va de 0 a 1.
La función get_water() devuelve el nivel de agua del suelo sobre el que se encuentra.

La velocidad de crecimiento de una planta escala linealmente desde una velocidad de 1x con un nivel de agua de 0 hasta una velocidad de 5x con un nivel de agua de 1.

El suelo se seca con el tiempo: de media, pierde el 1% de su agua actual por segundo, pero hay cierta variación aleatoria en esto.
Mantener un nivel de agua alto consumirá mucha más agua que mantener un nivel de agua bajo.

Puedes usar agua en tus plantas. Se añade automáticamente un tanque de agua a tu inventario cada 10 segundos.
Mejorar Unlocks.Watering duplicará la cantidad de agua que obtienes cada 10 segundos.

Un tanque contiene 0.25 de agua.

Llama a use_item(Items.Water) sobre cualquier suelo para regar el terreno.

# Funciones integradas

## can_harvest()
can_harvest()
Se usa para saber si las plantas han crecido completamente.

devuelve True si hay una entidad debajo del dron lista para ser cosechada, False en caso contrario.

tarda 1 tick en ejecutarse.

ejemplo:
if can_harvest():
    harvest()

Para más información relacionada, consulta: [Speed](#mejora-de-velocidad)

## can_move(direction)
Comprueba si el dron puede moverse en la direction especificada.

devuelve True si el dron puede moverse, False en caso contrario.

tarda 1 tick en ejecutarse.

ejemplo:
if can_move(North):
    move(North)

Para más información relacionada, consulta: [Mazes](#laberintos)

## change_hat(hat)
Cambia el sombrero del dron a hat.

devuelve None

tarda 200 ticks en ejecutarse.

ejemplo:
change_hat(Hats.Dinosaur_Hat)

## clear()
Elimina todo de la granja, mueve el dron de vuelta a la posición (0,0) y cambia el sombrero de nuevo al sombrero de paja.

devuelve None

tarda 200 ticks en ejecutarse.

ejemplo:
clear()

Para más información relacionada, consulta: [Plant](#plantar)

## dict(dictionary = None)
Crea un nuevo diccionario.
Si dictionary es None, crea un diccionario vacío.
Si dictionary es un diccionario, crea una copia de él.

devuelve un diccionario.

tarda 1 + len(dictionary) ticks en ejecutarse.

ejemplo:
new_dict = dict()

Para más información relacionada, consulta: [Dicts](#diccionarios)

## do_a_flip() 
¡Hace que el dron dé una voltereta! Esta acción no se ve afectada por las mejoras de velocidad.

devuelve None

tarda 1s en ejecutarse.

ejemplo:
while True:
    do_a_flip()

## get_companion()
Obtiene el compañero preferido de la planta debajo del dron.

devuelve una tupla de la forma (companion_type, (companion_x_position, companion_y_position))

tarda 1 tick en ejecutarse.

ejemplo:
companion = get_companion()
if companion != None:
    plant_type, (x, y) = companion
    print("Companion:", plant_type, "at", x, ",", y)

Para más información relacionada, consulta: [Polyculture](#policultivo)

## get_entity_type()
Averigua qué tipo de entidad hay debajo del dron.

devuelve None si la casilla está vacía, de lo contrario devuelve el tipo de la entidad debajo del dron.

tarda 1 tick en ejecutarse.

ejemplo:
if get_entity_type() == Entities.Grass:
    harvest()

Para más información relacionada, consulta: [Senses](#sentidos)

## get_ground_type()
Averigua qué tipo de terreno hay debajo del dron.

devuelve el tipo del terreno debajo del dron.

tarda 1 tick en ejecutarse.

ejemplo:
if get_ground_type() != Grounds.Soil:
    till()

Para más información relacionada, consulta: [Senses](#sentidos)

## get_pos_x() 
Obtiene la posición x actual del dron.
La posición x comienza en 0 en el oeste y aumenta en dirección este.

devuelve un número que representa la coordenada x actual del dron.

tarda 1 tick en ejecutarse.

ejemplo:
x, y = get_pos_x(), get_pos_y()

Para más información relacionada, consulta: [Senses](#sentidos)

## get_pos_y()
Obtiene la posición y actual del dron.
La posición y comienza en 0 en el sur y aumenta en dirección norte.

devuelve un número que representa la coordenada y actual del dron.

tarda 1 tick en ejecutarse.

ejemplo:
x, y = get_pos_x(), get_pos_y()

Para más información relacionada, consulta: [Senses](#sentidos)

## get_tick_count()
Se usa para medir el número de ticks realizados.

devuelve el número de ticks realizados desde el inicio de la ejecución.

tarda 0 ticks en ejecutarse.

ejemplo:
do_something()

print(get_tick_count())

Para más información relacionada, consulta: [Timing](#medición-de-tiempo)

## get_time() 
Obtiene el tiempo de juego actual.

devuelve el tiempo en segundos desde el inicio del juego.

tarda 0 ticks en ejecutarse.

ejemplo:
start = get_time()

do_something()

time_passed = get_time() - start

Para más información relacionada, consulta: [Timing](#medición-de-tiempo)

## get_water() 
Obtiene el nivel de agua actual debajo del dron.

devuelve el nivel de agua debajo del dron como un número entre 0 y 1.

tarda 1 tick en ejecutarse.

ejemplo:
if get_water() < 0.5:
    use_item(Items.Water)

Para más información relacionada, consulta: [Watering](#riego)

## get_world_size()
Obtiene el tamaño actual de la granja.

devuelve la longitud del lado de la cuadrícula en la dirección de norte a sur.

tarda 1 tick en ejecutarse.

ejemplo:
for i in range(get_world_size()):
    move(North)

## harvest()
Cosecha la entidad debajo del dron. 
Si cosechas una entidad que no se puede cosechar, será destruida.

devuelve True si se eliminó una entidad, False en caso contrario.

tarda 200 ticks en ejecutarse si se eliminó una entidad, 1 tick en caso contrario.

ejemplo:
harvest()

## has_finished(drone)
Comprueba si el drone especificado ha terminado.

devuelve True si el drone ha terminado, False en caso contrario.

tarda 1 tick en ejecutarse.

ejemplo:
drone = spawn_drone(function)
while not has_finished(drone):
    do_something_else()
result = wait_for(drone)

Para más información relacionada, consulta: [Megafarm](#megagranja)

## len(collection) 
Obtiene el número de elementos en una lista, conjunto, diccionario o tupla.

devuelve la longitud de la collection.

tarda 1 tick en ejecutarse.

ejemplo:
for i in range(len(list)):
    list[i] += 1

Para más información relacionada, consulta: [Lists](#listas)

## list(collection = None)
Crea una nueva lista. 
Si collection es None, crea una lista vacía.
Si collection es cualquier secuencia, crea una nueva lista con los elementos de la secuencia.

devuelve una lista.

tarda 1 + len(collection) ticks en ejecutarse.

ejemplo:
new_list = list((1,2,3))

Para más información relacionada, consulta: [Lists](#listas)

## max_drones()
devuelve el número máximo de drones que puedes tener en la granja.

tarda 1 tick en ejecutarse.

ejemplo:
while num_drones() < max_drones():
    spawn_drone(task)
    move(East)

Para más información relacionada, consulta: [Megafarm](#megagranja)

## measure(direction = None) 
Puede medir algunos valores en algunas entidades. El efecto de esto depende de la entidad.

Si direction no es None, mide la entidad vecina en la dirección dada.

devuelve el número de pétalos de un girasol.
devuelve la siguiente posición para un tesoro o una manzana.
devuelve el tamaño de un cactus.
devuelve un número misterioso para una calabaza.
devuelve None para todas las demás entidades.

tarda 1 tick en ejecutarse.

ejemplo:
num_petals = measure()

Para más información relacionada, consulta: [Sunflowers](#girasoles)

## move(direction)
Mueve el dron en la direction especificada una casilla.
Si el dron se mueve sobre el borde de la granja, reaparece en el otro lado.

East   =  derecha
West   =  izquierda
North  =  arriba
South  =  abajo

devuelve True si el dron se ha movido, False en caso contrario.

tarda 200 ticks en ejecutarse si el dron se ha movido, 1 tick en caso contrario.

ejemplo:
move(North)

Para más información relacionada, consulta: [Expand_1](#expansión-1)

## num_drones()
devuelve el número de drones actualmente en la granja.

tarda 1 tick en ejecutarse.

ejemplo:
while num_drones() < max_drones():
    spawn_drone(task)
    move(East)

Para más información relacionada, consulta: [Megafarm](#megagranja)

## num_items(item) 
Averigua qué cantidad del item tienes actualmente.

devuelve el número del item que tienes actualmente en tu inventario.

tarda 1 tick en ejecutarse.

ejemplo:
if num_items(Items.Fertilizer) > 0:
    use_item(Items.Fertilizer)

Para más información relacionada, consulta: [Senses](#sentidos)

## num_unlocked(thing)
Se usa para comprobar si un desbloqueo, entidad, terreno, ítem o sombrero ya está desbloqueado.

devuelve 1 más el número de veces que thing ha sido mejorado si thing es mejorable. De lo contrario, devuelve 1 si thing está desbloqueado, 0 en caso contrario.

tarda 1 tick en ejecutarse.

ejemplo:
plant(Entities.Bush)
n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
use_item(Items.Weird_Substance, n_substance)

Para más información relacionada, consulta:[Senses](#sentidos)

## pet_the_piggy() 
¡Acaricia al cerdito! Esta acción no se ve afectada por las mejoras de velocidad.

devuelve None

tarda 1s en ejecutarse.

ejemplo:
while True:
    pet_the_piggy()

## plant(entity)
plant(entity) 
Gasta el coste de la entity especificada y la planta debajo del dron.
Falla si no puedes permitirte la planta, el tipo de terreno es incorrecto o ya hay una planta ahí.

devuelve True si tuvo éxito, False en caso contrario.

tarda 200 ticks en ejecutarse si tuvo éxito, 1 tick en caso contrario.

ejemplo:
plant(Entities.Bush)

## print(*args) 
Imprime todos los args en el aire sobre el dron usando humo. Esta acción no se ve afectada por las mejoras de velocidad.
Se pueden imprimir múltiples valores a la vez.

devuelve None

tarda 1s en ejecutarse.

ejemplo:
print("ground:", get_ground_type())

Para más información relacionada, consulta: [Debug](#depuración)

## quick_print(*args)
Imprime un valor igual que print(*args) pero no se detiene para escribirlo en el aire, por lo que solo se puede encontrar en la página de salida.

devuelve None

tarda 0 ticks en ejecutarse.

ejemplo:
quick_print("hi mom")

Para más información relacionada, consulta: [Debug](#depuración)

## range(start = 0, end, step = 1)
Genera una secuencia de números que empieza en start, termina justo antes de alcanzar end (por lo que end se excluye) usando pasos de tamaño step.

Ten en cuenta que start se establece en 0 por defecto, y si solo se proporciona un argumento, se asignará a end. Esto normalmente no es posible.
En Python, range es un constructor de clase que permite este comportamiento extraño.

tarda 1 tick en ejecutarse.

ejemplo:
for i in range(10):
    print(i)

for i in range(2,6):
    print(i)

for i in range(10, 0, -1):
    print(i)

## set(collection = None)
Crea un nuevo conjunto.
Si collection es None, crea un conjunto vacío.
Si collection es una colección de valores, crea un nuevo conjunto con esos valores.

devuelve un conjunto.

tarda 1 + len(collection) ticks en ejecutarse.

ejemplo:
new_set = set((1,2,3))

Para más información relacionada, consulta: [Dicts](#diccionarios)

## set_execution_speed(speed)
Limita la velocidad a la que se ejecuta el programa para ver mejor lo que está sucediendo.

Una speed de 1 es la velocidad que tiene el dron sin ninguna mejora de velocidad.
Una speed de 8 hace que el código se ejecute 8 veces más rápido y corresponde a la velocidad del dron después de 3 mejoras de velocidad.
Una speed de 0.5 hace que el código se ejecute a la mitad de la velocidad sin mejoras de velocidad. Esto puede ser útil para ver lo que está haciendo el código.

Si la speed es más rápida de lo que la ejecución puede ir actualmente, simplemente irá a la velocidad máxima.

Si la speed es 0 o negativa, la velocidad se cambia de nuevo a la velocidad máxima.
El efecto también se detendrá cuando la ejecución se detenga.

devuelve None

tarda 200 ticks en ejecutarse.

ejemplo:
set_execution_speed(1)

Para más información relacionada, consulta: [Debug2](#depuración-2)

## set_world_size(size)
Limita el tamaño de la granja para ver mejor lo que está sucediendo.
También limpia la granja y restablece la posición del dron.
Establece la granja a una cuadrícula de size x size.
El size más pequeño posible es 3.
Un size menor que 3 cambiará la cuadrícula de nuevo a su tamaño completo.
El efecto también se detendrá cuando la ejecución se detenga.

devuelve None

tarda 200 ticks en ejecutarse.

ejemplo:
set_world_size(5)

Para más información relacionada, consulta: [Debug2](#depuración-2)

## spawn_drone(function, *args)
Genera un nuevo dron en la misma posición que el dron que ejecutó el comando spawn_drone(function, *args). El nuevo dron comienza a ejecutar la función especificada. El resto de los argumentos se copian y se pasan a la función especificada. Después de que el dron termina, desaparecerá automáticamente.

devuelve el identificador del nuevo dron o None si todos los drones ya están generados.

tarda 200 ticks en ejecutarse si se generó un dron, 1 en caso contrario.

ejemplo:
def harvest_column(message):
    for _ in range(get_world_size()):
        harvest()
        move(North)
    print(message)

i = 0
while True:
    if spawn_drone(harvest_column, i):
        move(East)
        i = (i + 1) % 10

Para más información relacionada, consulta: [Megafarm](#megagranja)

## str(object)
devuelve una representación en formato de texto (string) del object.

tarda 1 tick en ejecutarse.

ejemplo:
string = str(1000)

Para más información relacionada, consulta: [Debug](#depuración)

## swap(direction)
Intercambia la entidad debajo del dron con la entidad al lado del dron en la direction especificada.
No funciona en todas las entidades.
También funciona si una (o ambas) de las entidades son None.

devuelve True si tuvo éxito, False en caso contrario.

tarda 200 ticks en ejecutarse si tuvo éxito, 1 tick en caso contrario.

ejemplo:
swap(North)

Para más información relacionada, consulta: [Cactus](#cactus)

## till()
Labra el suelo debajo del dron convirtiéndolo en Grounds.Soil. Si ya es tierra labrada, cambiará el suelo de nuevo a Grounds.Grassland.

devuelve None

tarda 200 ticks en ejecutarse.

ejemplo:
till()

Para más información relacionada, consulta: [Carrots](#zanahorias)

## use_item(item, n=1) 
Intenta usar el item especificado n veces. Solo se puede usar con algunos ítems, incluyendo Items.Water, Items.Fertilizer.

devuelve True si se usó un ítem, False en caso contrario.

tarda 200 ticks en ejecutarse si tuvo éxito, 1 tick en caso contrario.

ejemplo:
use_item(Items.Fertilizer)

Para más información relacionada, consulta: [Watering](#riego)

## wait_for(drone)
Espera hasta que el drone dado termine.

devuelve el valor de retorno de la función que el drone estaba ejecutando.

tarda 1 tick en ejecutarse si el drone esperado ya ha terminado.

ejemplo:
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
handle = spawn_drone(zero_arg_wrapper)
print(wait_for(handle))

Para más información relacionada, consulta: [Megafarm](#megagranja)

# Items

## Hay (Hierba)
Se obtiene al cortar hierba.

## Wood
Se obtiene de arbustos y árboles.
Para más información relacionada, consulta: [Plant](#plantar)

## Carrot
Se obtiene al cosechar zanahorias.
Para más información relacionada, consulta: [Carrots](#zanahorias)

## Pumpkin
Se obtiene al cosechar calabazas.
Para más información relacionada, consulta: [Pumpkins](#calabazas)

## Cactus
Se obtiene al cosechar cactus ordenados.

## Weird_Substance
Llama a use_item(Items.Weird_Substance) en un arbusto para hacer crecer un laberinto, o en otras plantas para alternar su estado de infección. Se obtiene de plantas infectadas. Fertilizar plantas las infecta.
Para más información relacionada, consulta: [Fertilizer](#fertilizante)

## Gold
Se encuentra en cofres del tesoro en los laberintos.
Para más información relacionada, consulta: [Mazes](#laberintos)

## Water
Se usa para regar el suelo llamando a use_item(Items.Water)
Para más información relacionada, consulta: [Watering](#riego)

## Fertilizer
Llama a use_item(Items.Fertilizer) para reducir instantáneamente en 2s el tiempo de crecimiento restante de las plantas.

## Power
Se obtiene al cosechar girasoles. El dron lo usa automáticamente para moverse el doble de rápido.
Para más información relacionada, consulta: [Sunflowers](#girasoles)

# Entidades

## Bush
asda

## Cactus
Los cactus vienen en 10 tamaños diferentes. Al cosechar, los cactus adyacentes que estén "ordenados" también serán cosechados.

Tiempo de crecimiento base entre 1 y 1 segundos.
Puede crecer en soil.

**Coste de la Planta**
- Pumpkin 64


## Carrot
Tiempo de crecimiento base entre 4.8 y 7.2 segundos.
Puede crecer en soil.

**Coste de la Planta**
- Hay(hierba) 512
- Wood 512

Para más información relacionada, consulta: [Carrots](#zanahorias)

## Dead_Pumpkin
Una de cada cinco calabazas muere cuando crece, dejando atrás una calabaza muerta. Las calabazas muertas son inútiles y desaparecen cuando se planta algo nuevo.

Para más información relacionada, consulta: [Pumpkins](#calabazas)

## Grass
Crece automáticamente en praderas. Cosecharla para obtener Items.Hay.

Tiempo de crecimiento base entre 0.5 y 0.5 segundos.
Puede crecer en soil or grassland.

## Hedge
Parte del laberinto.

**Coste de la Planta**
- Weird_substance 4

Para más información relacionada, consulta: [Mazes](#laberintos)

## Pumpkin
Las calabazas crecen juntas cuando están al lado de otras calabazas completamente crecidas. Aproximadamente 1 de cada 5 calabazas muere cuando crece.

Tiempo de crecimiento base entre 0.2 y 3.8 segundos.
Puede crecer en soil.

**Coste de la Planta**
- Carrot 512

Para más información relacionada, consulta: [Pumpkins](#calabazas)

## Sunflower
Los girasoles recogen la energía del sol. Cosecharlos te dará Items.Power.
Si cosechas un girasol con el número máximo de pétalos, obtienes energía extra.

Tiempo de crecimiento base entre 5.6 y 8.4 segundos.
Puede crecer en soil.

**Coste de la Planta**
- Carrot 1

## Treasure
Un tesoro que contiene oro igual a la longitud del lado del laberinto en el que está escondido. Se puede cosechar como una planta.

**Coste de la Planta**
- Weird_substance 4

Para más información relacionada, consulta: [Mazes](#laberintos)

## Tree
Los árboles sueltan más madera que los arbustos. Tardan más en crecer si otros árboles crecen a su lado.

Tiempo de crecimiento base entre 5.6 y 8.4 segundos.
Puede crecer en soil or grassland.

Para más información relacionada, consulta: [Trees](#arboles)

# Terrenos

## Grassland
El terreno por defecto. La hierba crecerá automáticamente sobre él.

## Soil
Llamar a till() convierte el terreno en tierra de cultivo. Volver a llamar a till() lo convierte de nuevo en pradera.