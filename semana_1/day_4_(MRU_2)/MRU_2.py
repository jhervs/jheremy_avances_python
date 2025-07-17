#✨2da Version del simulador de MRU 📘

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

#inicio e introduccion.
again = "si"

while again == "si":
    try:
        input(""" 
Hola Usuario ☺️🩵. Bienvenido a este simulador de MRU.
Aqui te ayudaremos a resolver tus ejercicios en base
al dato que necesites hallar. Solo necesitas igresar
los datos que tienes, y el resto lo hago yo 🤓. 

Ingresa "si" para iniciar 🤓 o "no" para dejarlo para otro dia 🥹.
\n
""")
    except ValueError:
        print("Lo sentimos, el valor ingresado no es valido 😵‍💫.\n Vuelve a intentar ☺️✨\n")
    else: #Opciones de operaciones y condicionales
        us_op = False
        while us_op == False:
            try:
                us_op = input("""
Comencemos 🤓💪. Ahora necesito que ingreses
la operacion que quieres realizar. Buscar distancia,
buscar velocidad o tiempo:

1.Ingresa "d" para distancia 🎈.
2.Ingresa "v" para velocidad 🥏.
3.Ingresa "t" para tiempo 🕰️.\n
""")
            except ValueError:
                print("Opps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️")
            else:
                if us_op == "d":
                    valid_2 = False
                    while valid_2 == False:
                        try:
                            v = float(input("Muy bien ☺️✨. Ahora ingresa el valor de velocidad 🥏"))
                            t = float(input("Ahora, ingresa el valor del tiempo 🕰️"))
                        except ValueError:
                            print("Opps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️")
                            print(f"La distancia 🎈 del objeto es de {op_d(v, t)} metros 🤓☝️.")
                        else:
                            if us_op == "v":
                                valid_3 = False
                                while valid_3 == False:
                                    try:
                                        d = input("Muy bien ☺️✨. Ahora ingresa el valor de la distancia 🎈")
                                        t = input("Ahora, ingresa el valor del tiempo 🕰️")
                                    except ValueError:
                                        print("Opps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️")
                                        print(f"La valocidad 🥏 del objeto es de {op_v(d, t)} m/s 🤓☝️.")
                                    else:
                                        if us_op == "t":
                                            valid_4 = False
                                            while valid_4 == False:
                                                try:
                                                    d = input("Muy bien ☺️✨. Ahora ingresa el valor de la distancia 🎈")
                                                    v = input("Ahora, ingresa el valor de velocidad 🥏")
                                                except ValueError:
                                                    print("Opps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️")
                                                    print(f"El tiempo 🕰️ del objeto es de {op_t(d, v)} metros 🤓☝️.")
else:
    print("De acuerdo ☺️, resolvemos problemas otra ocasion 🥹 🩵")



