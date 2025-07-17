""" 
Mini reto (para entrenar la logica de tu futuro simulador)

Haz que el usuario ingrese dos valores y calcule el
tercero automáticamente. Por ejemplo:

# Ejemplo:
# Ingresa velocidad: 10
# Ingresa tiempo: 5
# Resultado: Distancia = 50 m

"""

print("""
Hola usuario. Bienvenido a tu programa de solucion
de ejercicios MRU 🤓.

Los datos validos para este programa son:

1.Velocidad.
2.Tiempo.
3.Distancia.

Al ingresar otro marcara error el programa. 😯\n
""")

us_op = input("""
Dime. ¿Que datos necesitas encontrar?

1. v
2. t
3. d

Coloca la letra de la opcion que necesites. 🤓
""").lower()

val_1 = int(input("Empecemos. Ingresa el primer dato que tenga "))

val_2 = int(input("Ingresa tu segundo dato. "))


if us_op == "v":
    print(f"la velocidad de tu objeto es de {val_1 / val_2} m/s")

elif us_op == "t":
    print(f"El tiempo de tu objeto es de {val_1 / val_2} s")

elif us_op == "d":
    print(f"La distancia recorrida de tu objeto es de {val_1 * val_2} m")
else:
    print("Lo sentimos, a segurate de ingresar los datos correctos")


""" 
Bueno, esto es todo por hoy, hay algunas cositas que
me gustaria mejorar para asi evitar errores como 
condicionar al usuario que el primer valos sea siempre
el dato "d", claro puedo colocar un comentario de 
recordatorio que cuando vas a calcular otro dato que no
sea distancia, en la division de los otros datos 
la distancia siempre va arriba, pero creo que necesitaria 
re-escribirlo para hacer que ese tipo de errores se puedan 
evitar y asi no se le da un resultado erroneo al usuario.

Pero ya sera en la proxima edicion jeje 🤓🩵.
"""