#Conversor de unidades.

""" 
Convierte de kilometros a metros,
(1km = 1000m) o de celsius a fahrenheit:

Formula:

fahrenheit = (celsius * 9/5) + 32

💡 Requisitos del ejercicio:
Usar input() para pedir el valor al usuario

Hacer la conversión matemática correcta

Usar print() con F-strings para mostrar el resultado

(Opcional) Comentar cada paso como hiciste antes
"""

print("""
Hola usuario. Hagamos la conversion 
de celsius a fahrenheit UvU!!      
""")

temp_c = int(input("Ingresa la temperatura a convertir \n")) #type<'int'>

convert = (temp_c * 9/5) + 32 #type<float>

print(f"La temperatura ingresada a Fahrenheit es {convert} grados Fahrenheit")

""" 
En este ejercicio realizamos una operacion
sencilla usando los operadores que vimos mas 
la funcion de tipo y el input para que el 
programa interactue con el usuario. Ya mas adelante 
se podria hacer algo un poco mas complejo, añadiendo
distintos de conversiones y asi darle a escojer al
usuario.
"""