""" 
necesitamos resolver los siguientes 
ejercicios:

1.v = 12 m/s, t = 5 s → ¿d?
2.d = 150 m, v = 10 m/s → ¿t?
3.d = 100 m, t = 20 s → ¿v?

recuerda las formulas:

Distancia:

d = v * t

Tiempo:

t = d/v

Velocidad:

v = d/t

Empecemos🤓
"""


#Ejercicio 1.

#datos:

v = 12 #type<'int'>

t = 5  #type<'int'>

#necesitamos:

#d = ?

#Ejecucion:

d = v * t #type<'int'>

print(f"La distancia recorrida de nuestro objeto es de {d} m\n")

#Ejercicio 2.

#datos:

d = 150 #type<'int'>

v = 10 #type<'int'>

#necesitamos:

#t = ?

#Ejecucion:

t = int(d / v) #type<'int'>

print(f"El tiempo recorrido de nuestro objeto es de {t} s\n")

#Ejercicio 3.

#datos:

d = 100 #type<'int'>

t = 20 #type<'int'>

#necesitamos:

#v = ?

#Ejecucion:

v = int(d / t) #type<'int'>

print(f"La velocidad de nuestro objeto es de {v} m/s")


""" 
Bueno, como pueden ver estos han sido los ejercicios
practicos de MRU, bastantes sencillos, usamos las 
funciones que se aprendieron ayer, como son:

la funcion de tipo.
la concatenacion con F-string
realizamos operaciones basicas las cuales 
ya estan integradas en python 
y comentamos.

Algo que me paso por la cabeza es que con esto 
se podria hacer un programa que solucione
ejercicios de MRU, usando input para pedir los
datos con los que cuenta el usuario, poniendo 
condiciones en base a los datos, tanto los que tiene
como los que no, creo que de eso se trata este primer
proyecto de simulacion.
"""