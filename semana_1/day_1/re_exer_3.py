#Ejercicio 3 (Año de Nacimiento)

""" 
📋 Requisitos del ejercicio:

1.Pedir al usuario su nombre

2.Pedir su edad actual (int)

3.Pedir el año actual (int)

4.Calcular su año de nacimiento con la fórmula:

Año de nacimiento = año actual - edad

5.Mostrar el resultado con un f-string
"""


print("""

Hola usuario. Bienvenido a este programa interactivo
donde descubriremos en que año naciste con solo dos 
datos tuyos, o de otra persona 🫢;necesitamos
la edad actual y el año actual 😯✨. Empecemos. 😌✨\n
""")

edad = int(input("Ingresa la edad actual \n")) #type<'int'>

año = int(input("Ahora, ingresa el año actual \n")) #type<'int'>

naci = año - edad #type<'int'>

print(f"Ahora estamos listos ☺️, el año de nacimiento es {naci}")

""" 
Bueno, en este ejercicio practico, usamos los 
fundamentos basicos de python, como son las 
variables, funciones como "int()", inputs,
comentarios y operaciones matematicas basicas, 
tambien un F-string, para hacer un mensaje final
concatenando la variable que tiene la operacion.
Algo de lo cual nos puede servir saber como hacer
este tipo de programas, es para saber como sirve 
un logeo en una pagina, donde el programa 
pide al usuario que llene formularios, y en base 
a ello el programa va crando una base de datos del 
usuario, guardandolo en su sistema y asi ya el 
usario contaria con sus credenciales de acceso a la
pagina, claro este ejemplo, es bastante simple, pero
la base de todo programa comienza desde lo basico y
simple, y de ahi se va escalando ☺️✨, esto es lo 
que opino como conclusion del ejercicio ✨🤓
"""