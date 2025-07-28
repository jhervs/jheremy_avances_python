#Diseño de flujo (To-do list project)


#definimos funciones


def bienvenida(): #da una bienvenida
    print("""
Hola usuario ☺️✨. Bienvenido a tu to-do list
personal ¿Que vas hacer hoy? 🤔📘
""")

tareas = {} #type<'dict'> almacena las tareas


def hacer_tarea(): #crea la tarea
    nombre = input("\nIngresa el nombre de la tarea ☺️ ✏️\n")
    if nombre in tareas:
        print("\nOops 😵‍💫. Tarea existente, ingresa otro nombre ☺️\n")
        return
    
    fecha = input("\nAhora, ingresa una fecha limite para tu tarea (DD/MM/YYYY)☺️ 📅\n")
    nota = input("\nIngresa una nota para tu tarea ☺️ 📘 \n")

    tareas[nombre] = {
        "fecha": fecha,
        "nota": nota,
        "estado": "pendiente"
    }

    print(f"Tarea {nombre} creada con exito ☺️📅✨")

def mostras_tareas():
    print(tareas)


while True:
    bienvenida()
    opciones = input("""\n
Aqui te dejo las opciones que tienes para escoger:

1. Crear una tarea 📅🩵
2. Mostras tareas actuales 📘 ✏️
3. Nada por hoy. Salir 👋☺️\n
""")
    if opciones == "1":
        hacer_tarea()
        again = input("""\n
¿Quieres seguir añadiendo tareas? 🤔✨
escribe:

si (Para seguir 💪📅)
no (Para salir 👋☺️ 🩵)\n
""".lower())
        if again == "si":
            print("\nSigamos agregando tareas 💪📅\n")
            continue
        else:
            print()
            break
    elif opciones == "2":
        print("\nEstas son tus tareas actuales ☺️ 🩵: \n")
        mostras_tareas()
        again_1 = input("""
Muy bien ☺️ 🩵 ¿Quieres realizar otra operacion?

Ingresa "si" para continuar
ingresa "no" para culminar.
""")
        if again_1 == "si":
            print("\nDe acuerdo, sigamos ☺️ ✨\n")
            continue
        else:
            print("Muy bien, Terminamos por ahora 🥹 🩵")
            break
    elif opciones == "3":
        print("De acuerdo ☺️. Sera para la proxima ✨ 🩵")
        break 
    else:
        print("lo sentimos 😔. El valor ingresado no es valido. Vuelve a intentar ☺️ 🩵")


""" 
En este programa hacemos uso de variables, funciones
y herramientas basicas y un poco mas complejas de python.

usamos variables sencillas, funciones como print() y lower().

Tambien herramienta de control de flujo, como es break,
continue y return. 

Tambien hacemos uso de condicionales como (if, elif, else)
y bucles con while.

Y algo importante y nuevo que hacemos uso aqui es el dato
tipo diccionario el cual nos ayuda a almacenar las tareas.

este es un tipo de dato, que nos ayuda a almacenar valores,
ya sea str o numerico (si no me equivoco), y la ventaja de 
usar diccionarios, es que este es mutables y no permite
valores (claves "nombres") repetidos, lo cual nos ayuda a 
que el programa sea ordenado. Claro tanbien usamos otros 
datos, pero esos ya son los tipo primitivos, (int, str, bool..etc)


Conlusion:
Este programa es un programa "sencillo" aun que claro que se 
puede complicar si no creas un buen flujo o si no planteas 
un algoritmo logico y funcional. Por eso plantar el flujo
en una hoja, aun que sientas que es perdida de tiempo,
te puede ayudar a que en tu mente el programa ya tenga un orden
claro, y asi evitas perderte en el codigo, cosa que me paso mucho
en el proyecto anterior, pero haber pasado eso me ayudo mucho
a como afrontar este tipo de flujo con while.

Nota: Algo si, voy a tener que retomar mi curso, ya que 
tengo que refrescar este tipo de datos, para asi hacer el
codigo con mas confianza. Pero bueno, vamos creciendo poco
a poco 💪🩵☺️
"""

