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

Ver también [Conjuntos](##con)

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


## Conjuntos