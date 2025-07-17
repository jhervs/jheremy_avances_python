#Calculadora Basica.

""" 
Pide al usuario dos numero y muestra:

1.Suma
2.Resta
3.Multiplicacion
4.Division
"""
print("Hola usuario :3. Primero ingresa los numeros que quieres calcular.\n")

num_1 = int(input("Ingresa tu primer numero ")) #type<'int'> + input

num_2 = int(input("Ingresa tu segundo numero ")) #type<'int'> + input

user_election = input("""
Ahora dime que operacion quieres realizar 
en base a estas opciones:

1. +
2. -
3. *
4. / .\n
""") #type<'str'> + input

if user_election == "+":
    print(num_1 + num_2)

elif user_election == "-":
    print(num_1 - num_2)

elif user_election == "*":
    print(num_1 * num_2)

elif user_election == "/":
    print(num_1 / num_2)

else:
    print("Lo sentimos usuario, no soportamos la operacion introducida. Xp")

""" 
Bueno, este es nuestro primer ejercicio realizado.
una calculadora basica.

para hacerla, los conceptos basicos del repaso, pero
le agregue los condicionales con if, elif y else, para
que asi sea mas didactica dando le la posibilidad de 
escoger al usuraio.
"""

#proximo a editar para mejorar