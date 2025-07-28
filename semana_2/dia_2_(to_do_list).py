#Projecto To-do list (1er modelo)

""" 
Programa: To-do list project
Autor: Jheremy 💻✨
Fecha: 22/07/2025 (Retomamos)

Introduccion: programa donde el usuario puede organizar sus tareas,
guardarlas, darle un dia limite y culminarla. 
"""

#diccionario

tareas = {}

#creamos funciones.

def bienvenida(): #da una bienvenida
    print("""
Hola usuario ☺️ ✨. Bienvenido a tu to-do list
personal ¿Que vas hacer hoy? 🤔 📘
""")

def seguir():
    again = input("""\n¿Quieres realizar otra tarea o accion? 🤔✨
escribe:

si (Para seguir 💪 📅)
no (Para salir 👋 ☺️ 🩵)\n""")
    return again == "si"

#op 1
def crea_tarea():
    nombre = input("\nIngresa el nombre de la tarea ☺️  ✏️\n")
    if nombre in tareas:
        print("\nOops 😵‍💫. Tarea existente, ingresa otro nombre ☺️\n")
        return
    
    fecha = input("\nAhora, ingresa una fecha limite para tu tarea (DD/MM/YYYY)☺️ 📅\n")
    nota =  input("\nIngresa una nota para tu tarea ☺️ 📘 \n")

    tareas[nombre] = {
        "fecha": fecha,
        "nota": nota,
        "estado": "pendiente"
    }

    print(f"\nTarea {nombre} creada con exito ☺️ 📅 ✨\n")

#op 2
def mostrar_tareas():
    if not tareas:
        print("\nNo hay tareas actualmente ☺️ ✨\n")
        return
    for nombre, datos in tareas.items():
        print(f"\n✏️  tarea {nombre}")
        for clave, valor in datos.items():
            print(f" {clave.capitalize()}: {valor}\n")

#op 3
def edit_tarea():
    print("\nEstas son las tareas actuales ☺️ ✏️: \n")
    mostrar_tareas()
    print("\n📌 *Recuerda escribir el nombre exactamente como lo escribiste (mayúsculas, tildes, etc.) ☺️ ✏️*\n")
    selec = input("\nIngresa el nombre de la tarea que editaras ☺️ ✨\n")
    if selec in tareas:
        print(f"\nEste es el estado de la tarea seleccionada 🤓 📘\n {tareas[selec]} \n")

        nombre = input("""\n
Ingrese el nombre nuevo de la tarea ☺️ ✨.
O ingresa el mismo por si no quieres editarlo 🤓\n
""")
        

        fecha = input("""\n
Ingrese la nueva fecha limite de la tarea ☺️ ✨,
si la quiere editar (DD/MM/YYYY)☺️ 📅\n
""")
        
        nota = input("""\n
Ingresa la nueva nota de la tarea ☺️ ✏️\n
""")
        if nombre != selec:
            tareas[nombre]= tareas.pop(selec)

        tareas[nombre]["fecha"]= fecha

        tareas[nombre]["nota"]= nota

        print(f"\nTarea {selec} ha sido editada satisfactoriamente ☺️ ✏️\n")
    else:
        print("\nOops 😵‍💫. La tarea ingresada no existe. Vuelve a intentarlo ☺️ ✏️\n")
        return

#op 4
def elim_tarea():
    print("\nEstas son las tareas actuales ☺️ ✏️: \n")
    mostrar_tareas()
    print("\n📌 *Recuerda escribir el nombre exactamente como lo escribiste (mayúsculas, tildes, etc.) ☺️ ✏️*\n")
    selec_1 = input("""\n
Indica cual es la tarea que quieres eliminar ingresando su nombre ☺️ ✏️.\n
""")
    if selec_1 in tareas:
        del tareas[selec_1]
        print("\nSe ha eliminado la tarea exitosamente ☺️ ✨\n")
        mostrar_tareas()
    else:
        print("\nOops 😵‍💫. La tarea ingresada no existe. Vuelve a intentarlo ☺️ ✏️\n")
        return

#op 5
def done():
    print("\nEstas son las tareas actuales 🤓 📘\n")
    mostrar_tareas()
    print("\n📌 *Recuerda escribir el nombre exactamente como lo escribiste (mayúsculas, tildes, etc.) ☺️ ✏️*\n")
    selec_2 = input("\nIngrese la tarea que ya ha realizado ☺️ 📘\n")
    if selec_2 in tareas:
        tareas[selec_2]["estado"]= "Finalizada"
        print(f"\nFelicidades ☺️ ✨ haz finalizado la tarea {selec_2}. Sigue asi 💪 🤓\n")
        mostrar_tareas()
    else:
        print("\nOops 😵‍💫. La tarea ingresada no existe. Vuelve a intentarlo ☺️ ✏️\n")
        return

#op 6
def posponer():
    print("\nEstas son las tareas actuales 🤓 📘\n")
    mostrar_tareas()
    print("\n📌 *Recuerda escribir el nombre exactamente como lo escribiste (mayúsculas, tildes, etc.) ☺️ ✏️*\n")
    selec_3 = input("\nIngrese la tarea que quieres posponer 🤔 📘\n")
    if selec_3 in tareas:
        fecha = input("\nAhora, ingresa la nueva fecha limite para tu tarea (DD/MM/YYYY) ✏️ 📅\n")
        tareas[selec_3]["fecha"] = fecha
        print(f"\nSe ha pospuesto la tarea {selec_3} con exito 🤓 ✏️\n")
        mostrar_tareas()
    else:
        print("\nOops 😵‍💫. La tarea ingresada no existe. Vuelve a intentarlo ☺️ ✏️\n")
        return

#op 7
def salir():
    print("De acuerdo ☺️. Ha sido un gusto verte por aqui ✨ 🩵")


while True:
    bienvenida()
    opciones = input("""\n
Aqui te dejo las opciones que tienes para escoger:

1. Crear una tarea 📅 🩵
2. Mostrar tareas actuales 📘
3. Editar tareas ✏️ 📘
4. Eliminar tarea 🗑️ 📘
5. Finalizar tarea 🤓 ✔️
6. Posponer tarea 📅 ✏️
7. Nada por hoy. Salir 👋 ☺️

Que haras hoy ☺️ ✨\n
""".strip())
    if opciones == "1":
        print("De acuerdo ☺️. Creemos tu tarea 🤓\n")
        crea_tarea()
        if seguir():
            print("\nMuy bien ✨, sigamos 💪 📅\n")
            continue
        else:
            print("\n Nos vemos en otra ocacion para crear mas tareas 👋 ☺️ ✨\n")
            break
    elif opciones == "2":
        print("\nAqui te muestros las tareas que tienes actualmente ☺️ 📅\n")
        mostrar_tareas()
        if seguir():
            print("\nMuy bien ✨, sigamos 💪 📅\n")
            continue
        else:
            print("\n Nos vemos en otra ocacion para crear mas tareas 👋 ☺️ ✨\n")
            break
    elif opciones == "3":
        print("Muy bien ✨, Empecemos a editar ☺️ ✏️")
        edit_tarea()
        if seguir():
            print("\nMuy bien ✨, sigamos 💪 📅\n")
            continue
        else:
            print("\n Nos vemos en otra ocacion para crear mas tareas 👋 ☺️ ✨\n")
            break
    elif opciones == "4":
        print("\nMuy bien ✨. Borremos la tarea 🗑️ 📘\n")
        elim_tarea()
        if seguir():
            print("\nMuy bien ✨, sigamos 💪 📅\n")
            continue
        else:
            print("\n Nos vemos en otra ocacion para crear mas tareas 👋 ☺️ ✨\n")
            break
    elif opciones == "5":
        print("\nFelicidades por tu avance. Empecemos ☺️ ✨\n")
        done()
        if seguir():
            print("\nMuy bien ✨, sigamos 💪 📅\n")
            continue
        else:
            print("\n Nos vemos en otra ocacion para crear mas tareas 👋 ☺️ ✨\n")
            break
    elif opciones == "6":
        print("\nDe acuesrdo ✨. Pospongamos tareas 🤓 📅\n")
        posponer()
        if seguir():
            print("\nMuy bien ✨, sigamos 💪 📅\n")
            continue
        else:
            print("\n Nos vemos en otra ocacion para crear mas tareas 👋 ☺️ ✨\n")
            break
    elif opciones == "7":
        salir()
        break
    else:
        print("\nOop 😵‍💫. Ha ocurrido un error, asegurate de ingresar un valor valido ☺️ ✨\n")

""" 
Bueno, por el momento ha sido el proyecto mas complejo que he hecho,
pero se me hizo mas facil a comparacion al anterior, creo que en parte
me ayudo mucho tener una idea previa de lo que se iba hacer, realizar
en mi cuaderno un paso a paso de lo que cada funcion iba hacer, como
tambien las funciones y herramientas que podria usar, me ayudaron
a sentirme mas suelto en el desarrollo del codigo. Hay algunas cosas
que se pueden mejorar, como el algoritmo de la parte de fecha en la 
funcion crear_tareas() ya que si meto cualquier dato se ejecuta, vendria
bien condicionar al usuario a solo ingresar la fecha, capas con banderas 
se podria hacer eso.

En conclusion, me siento bastante bien con mi avance, puede que aun tenga 
cosas que tal vez me estoy pasando, pero con lo que he probado, funciona
bien el programa, ya nos pondremos a corregir luego. Pero bueno, todo es
parte del progreso. Vamos con el siguiente proyecto ☺️✨
"""