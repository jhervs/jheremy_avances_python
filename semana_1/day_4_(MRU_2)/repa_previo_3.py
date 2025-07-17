#🧪 Mini Reto – Función con return

""" 
🎯 Objetivo:
Aprender a usar return para que una función devuelva un valor que luego puedas usar como tú quieras: mostrarlo, guardarlo, pasarlo a otra función, etc.

🧠 Enunciado:

1.Crea una función llamada generar_saludo(nombre)

2.En lugar de imprimir dentro de la función, usa return para devolver el saludo

3.Luego, en el programa principal:

4.Pide el nombre al usuario con input()

5.Llama a la función y guarda el saludo en una variable

6.Imprime el saludo usando print() fuera de la función
"""

""" 
Programa: Saludo Personalizado
Autor: Jheremy 💻✨
Fecha: 07/07/25

Introduccion: Este programa consiste en dar un saludo
personalizado al usuario, se ingresa el nombre, y este
da el saludo.
"""

#intento 3 (Logrado)

#definicion de funcion e inicio
def per_sal(nombre_2):
    return(f"Hola {nombre_2} ☺️ 🩵, me alegra mucho verte por aqui 🥹\n")

#se pide nombre
nombre_2 = input("Hola usuario. ☺️ ¿Dime cual es tu nombre? 🤔✨\n") #type<'str'> + input

#se declara la variable saludo y se reusa la funcion "per_sal"
saludo_2 = per_sal(nombre_2)

"""nota: Este tipo de funciones no imprimen, solo guardan una accion o operacion
por lo cual esta se tiene que usar con otras variables, como si fuera una suma.
"""

#imprime saludo y final.
print(saludo_2)

"""
Bueno, ha sido un ejercicio bastante interesante.
al principio no entendia como funcionaba el return,
hice dos intentos, uno siguiendo pasos en base a lo
que entendia, y el segundo segun lo que me parecia correcto,
pero aun asi no entendia, aun que sabia que algo estaba mal 
con mis ejercicio, asi que, la correccion es que,
primero intente usar la funcion sin el print, se puede,
per mi error es que el parametro añadido estaba afuera del 
return, por ende nunca se iba a mostrar, segundo, en el 
return ingresaba la propia funcion, claro, se regresa la 
funcion pero esta no tiene nada. Asi que buscando ayuda 
y comprendiendo realmente que es el return y que hace,
conclui de que es una manera de reusar alguna operacion 
o accion, este almacena una operacion o accion, haciendo
que esta la podamos usar en cualquier otro momento,
asi como podemos apreciar en el codigo, en nuestra funcion
tiene la accion de saludar al usuario, y la manera correcta 
hacer que esta accion sea reutilizable es ingresando
el parametro o accion al return. Y esa es la manera correcta 
usar el return. Mas abajo podran ver mis otros intentos.


#intento 1 (Fallido)

def sal_per(nombre):
    return(sal_per)

nombre = input("Hola usuario. ☺️ Dime cual es tu nombre 🤔✨\n")

sal_per(nombre)

saludo = (f"Hola {nombre} ☺️ 🩵, me alegra mucho verte por aqui \n🥹")

print(saludo)

#intento 2 (como creo que se haria "FALLIDO")

def saludo_per(nombre_1):
    (f"Hola {nombre_1} ☺️ 🩵, me alegra mucho verte por aqui 🥹\n")
    return(saludo_per)

nombre_1 = input("Hola usuario. ☺️ ¿Dime cual es tu nombre? 🤔✨\n")

saludo_per(nombre_1) 

"""