#1. Variables y tipos de datos.

""" 
Veremos algunos tipos de datos 
y como nombrar una variable.
"""

nombre = "Jheremy" #type<'str'> para texto
edad = 22 #type<'int'> numeros enteros
altura = 1.82 #type<'float'> numeros decimales
es_estudiante = True #type<'bool'> logicos, verdadero o falso

""" 
Estos son tipos de datos de python,
son estos datos basicos son conocidos
como datos de tipo primitivo, ya que
si no me equivoco, estos datos que comunmente
se repiten en los distintos lenguaje de 
programacion, solo que se diferencian por que
se llaman de otra manera y se escriben diferente,
lo cual depende de la sintaxis de cada lenguaje
de programacion. 
"""

#2. Entrada de datos (input()) y conversion de tipos.

print("Hola usurio. Rellena el siguientes formularios.\n")

nombre = input("¿Como te llamas? ") #type<'str'>
edad = int(input("¿Que edad tienes? ")) #type<'int'>

print(f"Hola {nombre}, tienes {edad} años.")


""" 
En esta parte del repaso, realizamos 
unas variables las cuales cuantan con 
la funcion input(), esta funcion nos 
sirve para pedirle informacion o datos
a los usuarios, dicha informacion se 
almacenara en una variable, como en este caso.

Tambien, vemos como realizar una conversion de tipaje
como podemos ver en la segunda variable, esta es una 
funcion de python las cuales se llaman funciones de tipo
o conversion.

Para finalizar, imprimimos la informacion del formulario
usando un F-string que es una manera de concatener datos 
o variables en una cadena de texto.
"""

#3. Operadores matematicos.

""" 
Este tercer punto, hablaremos sobre los 
operadores matematicos, que basicamente
nos sirven para realizar operaciones
matematicas, les pondre un ejemplo.
"""

suma = 2 + 2 #type<'int'> (result 4)
resta = 5 - 2 #type<'int'> (result 3)
multiplicacion = 3 * 4 #type<'int'> (result 12)
division = 7 / 2 #type<'float'> (result 3.5)

""" 
nota: la divisiones (/) siempre nos dara
como resultado una dato tipo "float", sin
importar que el resultado sea entero.
"""

division_entera = 7 // 2 #type<'int'> (result 3)

""" 
nota: A diferencia de la division normal,
este tipo de division siempre nos dara como
resultado, un numero entero, sin importar que
el resultado sea decimal ('float')
"""

modulo = 7 % 2 #type<'int'> (result 1)

"""
En este tipo de operacion ocurre lo siguiente,
esta operacion solo nos da como resultado el resto
de una division, por eso se llama modulo o resto.
Como podemos ver en el ejemplo de "7 % 2" nos da
como resultado 1, y eso es por que el numero divisible
entre 2 que se aproxime mas al 7 es el 6, y lo que
falta para llegar a 7 es un 1, y por eso el resultado.
"""

potencia = 2 ** 3 #type<'int'> (result 8)

""" 
En esta operacion, ocurre lo siguiente.
esta es como una multiplicacion normal,
solo que en vez de multiplicar el 2 por el 3
el dos se multiplica 3es veces. Ejemplo mas visual:

2 * 2 = 4 * (2) = 8

Como podemos apreciar, el dos se multiplico 3es veces 
dando asi el resultado "8".
"""

#4. imprimir resultados con formato (f-string)

nombre = "Jheremy" #type<'str'>
edad = 22 #type<'int'>

print(f"hola me llamo {nombre} y tengo {edad} años")

""" 
Esto fue algo que hicimos en un ejercicio
previo, pero en si al usar un f-string,
nos facilita imprimir de una manera mas
simple y rapida, nuestras variables en 
una sola linea de texto, como vemos en el
codigo. Es la manera mas actual de concatenar.
"""

#con esto culminamos el primer repaso rapido de este dia.