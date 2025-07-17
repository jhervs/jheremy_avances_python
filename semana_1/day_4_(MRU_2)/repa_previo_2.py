#🧪 Ejercicio 3 – Función personalizada con def.

""" 
Programa: Saludo Personalizado
Autor: Jheremy 💻
Fecha: 07/07/25

Introduccion: El programa realiza saludos personalizados.
el usuario introduce su nombre y este responde con un saludo.
"""
#inicio (definimos funcion)
def saludo(nombre):
    print(f"Hola {nombre}, es un guste verte por aqui ☺️ 🩵\n")

#pedimos nombre
nombre = input("Hola usuario ¿Cual es tu nombre? ☺️✨\n") #type<'str'> + input

#aplicamos la funcion
saludo(nombre)

""" 
Es un programa sencillo para poner en practica
como definir funciones, pero quiero acotar algo,
yo cometi un error el cual fue llamar la variable
con un print() para que apareciera en la terminal,
pero hubo un detalle que no estaba bien, y era que
al final me decia None, y esto era por que la funcion 
estaba vacia adentro del print. Ejemplo:

print(saludo()).

Y claro, despues pense, bueno, es una funcion, esta
daberia de mostrarse en la terminal sin necesidad de
usar un print(), y si es correcto, pero yo hice esto
saludo() y me marcaba error, el por que de eso era
que, cuando yo defini mi funcion, hice esto, "saludo(nombre)"
por ende cuando la colocaba mi funcion asi (saludo())
me daba error, ya que el interprete me dice:
TypeError: saludo() missing 1 required positional argument: 'nombre'
ya que la funcion estaba incompleta.

En conclusio: Cuando uno realice una funcion y
quieremos hacer que esta se muestre en la terminal
hay que escribirla tal cual como la definimos
ya sea saludo() o saludo(nombre), ambas estan bien
siempre y cuando la llamemos de la manera en que las
definimos.

Recomendacion, siempre agregarle un parametro a 
nuestras funciones. Ejemplo:

def saludo(nombre):
    print(f"Hola {nombre}, es un guste verte por aqui ☺️ 🩵\n")

"""