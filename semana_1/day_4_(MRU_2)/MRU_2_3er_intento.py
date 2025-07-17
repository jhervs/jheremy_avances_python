#✨3era Version del simulador de MRU 📘

""" 
Programa: Simulador de MRU
Autor: Jheremy💻✨
Fecha: 08/07/25

Introduccion: El programa consiste en resolver ejercicios de
MRU. El usuario selecciona la operacion a realizar, da los
datos, el programa resuelve y entrega el resultado.
"""
#Definimos funciones operacionales

def op_d(v, t):
    return v * t

def op_v(d, t):
    return d / t

def op_t(d, v):
    return d / v

def inicio():
    return input("""
Comencemos 🤓💪. Ahora necesito que ingreses
la operacion que quieres realizar. Buscar distancia,
buscar velocidad o tiempo:

1.Ingresa "d" para distancia 🎈.
2.Ingresa "v" para velocidad 🥏.
3.Ingresa "t" para tiempo 🕰️.\n
""")


def otra():
    return input(""" 
Hola Usuario ☺️ 🩵. Bienvenido a este simulador de MRU.
Aqui te ayudaremos a resolver tus ejercicios en base
al dato que necesites hallar. Solo necesitas igresar
los datos que tienes, y el resto lo hago yo 🤓. 

Ingresa "si" para iniciar 🤓 o "no" para dejarlo para otro dia 🥹.
\n
""")

again = otra()

user_op = inicio()

while again == "si":
    if user_op == "d":
        valid_v = False
        while valid_v is False:
            try:
                v = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de velocidad 🥏 \n"))
            except ValueError:
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
            else:
                valid_1 = False
                while valid_1 is False:
                    try:
                        t = float(input("\nAhora, ingresa el valor del tiempo 🕰️ \n"))
                    except ValueError:
                        print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    else:
                        print(f"La distancia 🎈 del objeto es de {op_d(v, t)} metros 🤓☝️.\n")
                        break
    elif user_op == "v":
        valid_2= False
        while valid_2 is False:
            try:
                d = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de distancia 🎈 \n"))
            except ValueError:
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
            else:
                valid_2 = False
                while valid_2 is False:
                    try:
                        t = float(input("\nAhora, ingresa el valor del tiempo 🕰️ \n"))
                    except ValueError:
                        print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    else:
                        print(f"La distancia 🎈 del objeto es de {op_v(d, t)} metros 🤓☝️.\n")
                        break
    elif user_op == "t":
        valid_3 = False
        while valid_3 is False:
            try:
                d = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de distancia 🎈 \n"))
            except ValueError:
                print("nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
            else:
                valid_3 = False
                while valid_3 is False:
                    try:
                        v = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de velocidad 🥏 \n"))
                    except ValueError:
                        print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    else:
                        print(f"\nEl tiempo 🕰️  del objeto es de {op_t(d, v)} segundos 🤓☝️.\n")
                        break
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""")
                    if again == "si":
                        print("\nMuy bien ☺️. Sigamos calculando datos 🤓 🩵.\n")
                        print(again)
                    else:
                        print("\nHa sido un gusto calcular el tiempo contigo. 🤓 🩵\n")
else:
    print("\nMuy bien ☺️. Resolvemos problemas otra ocasion 🥹 🩵\n")
