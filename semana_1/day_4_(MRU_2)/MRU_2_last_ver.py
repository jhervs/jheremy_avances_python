#✨Ultima Version del simulador de MRU 📘

""" 
Programa: Simulador de MRU
Autor: Jheremy💻✨
Fecha: 08/07/25

Introduccion: El programa consiste en resolver ejercicios de
MRU. El usuario selecciona la operacion a realizar, da los
datos, el programa resuelve y entrega el resultado.
"""
#Definimos funciones operacionales

def op_d(v, t): #operacion distancia
    return v * t

def op_v(d, t): #operacion velocidad
    return d / t

def op_t(d, v): #operacion tiempo
    return d / v

def inicio(): #funcion de inicio
    return input("""
Comencemos 🤓💪. Ahora necesito que ingreses
la operacion que quieres realizar. Buscar distancia,
buscar velocidad o tiempo:

1.Ingresa "d" para distancia 🎈.
2.Ingresa "v" para velocidad 🥏.
3.Ingresa "t" para tiempo 🕰️.\n
""").lower()

#declaracionde variable e inicio MRU
again = input(""" 
Hola Usuario ☺️ 🩵. Bienvenido a este simulador de MRU.
Aqui te ayudaremos a resolver tus ejercicios en base
al dato que necesites hallar. Solo necesitas igresar
los datos que tienes, y el resto lo hago yo 🤓. 

Ingresa "si" para iniciar 🤓 o "no" para dejarlo para otro dia 🥹.
\n
""").lower() 

#inicia bucle del programa
if again == "si":
    while True:
        user_op = inicio() #type<'str'>
        if user_op == "d": #condicionales de op_d
            try: #inicia analisis de errores
                v = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de velocidad 🥏 \n")) #type<'float'>
            except ValueError: #evaluacion del valor
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                continue
            else:
                try: #inicia analisis de errores
                    t = float(input("\nAhora, ingresa el valor del tiempo 🕰️ \n")) #type<'float'>
                except ValueError: #evaluacion del valor
                    print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    continue
                else: #entrega el resulatado
                    print(f"La distancia 🎈 del objeto es de {op_d(v, t)} metros 🤓☝️.\n") #type<'float'>
                    #reinicio o final
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""").lower
                    if again != "si":
                        print("\nHa sido un gusto calcular la distancia 🎈 🤓 🩵\n") #conclusion de op_d
                        break
        elif user_op == "v": #condicionales de op_v
            #inicia nota
            print("""\n
Nota: Asegurate de que el numerador (d) no sea cero (0),
ya que al dar el resultado dara error 😵‍💫. (No se puede dividir entre 0 🤓☝️).

Y si el denominador (t) es cero (0), el resultado
automaticamente sera 0. 🤓☝️\n
""")
            try:#inicia analisis de errores
                d = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de distancia 🎈 \n")) #type<'float'>
            except ValueError: #evaluacion del valor
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n") #type<'float'>
                continue
            else:
                try:#inicia analisis de errores
                    t = float(input("\nAhora, ingresa el valor del tiempo 🕰️ \n")) #type<'float'>
                except ValueError: #evaluacion del valor
                    print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n") #type<'float'>
                    continue
                else:#entrega el resulatado
                    print(f"La valocidad 🥏 del objeto es de {op_v(d, t)} m/s 🤓☝️.\n") #type<'float'>
                    #reinicio o final
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""").lower()
                    if again != "si":
                        print("\nHa sido un gusto calcular la velocidad 🥏 🤓 🩵\n") #conclusion de op_v
                        break
        elif user_op == "t":
            print("""\n
Nota: Asegurate de que el numerador (d) no sea cero (0),
ya que al dar el resultado dara error 😵‍💫. (No se puede dividir entre 0 🤓☝️).

Y si el denominador (v) es cero (0), el resultado
automaticamente sera 0. 🤓☝️\n
""")
            try: #inicia analisis de errores
                d = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de distancia 🎈 \n")) #type<'float'>
            except ValueError: #evaluacion del valor
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n") 
                continue
            else:
                try: #inicia analisis de errores
                    v = float(input("\nAhora, ingresa el valor de la velocidad 🥏 \n")) #type<'float'>
                except ValueError: #evaluacion del valor
                    print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    continue
                else:#entrega el resulatado
                    print(f"El tiempo del objeto es de {op_t(d, v)} segundos 🤓☝️.\n") #type<'float'>
                    #reinicio o final
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""").lower()
                    if again != "si":
                        print("\nHa sido un gusto calcular el tiempo 🕰️ 🤓 🩵\n") #conclusion de op_t
                        break
        else: #mensaje de error (seleccion de operacion)
            print("\nOops 😵‍💫. Algo ha salido mal. Vuelve a intentarlo ☺️ ✨")
else: #mensaje de despedida o de vuelve a intentarlo.
    print("""
\nMuy bien ☺️. Resolvemos problemas otra ocasion 🥹 🩵.
O asegurate de haber ingresado la respuesta correcta. ☺️🩵
\n""")


""" 
Conclusion:

Bueno, este ha sido mi primer proyecto como programador,
ha sido unos dias intensos de correccion y aprendizaje,
pero logre culminarlo, capaz no de la manera que tenia 
pensado, pero a causa de no tener por los momentos los
conocimientos necesarios, y el enfoque de este proyecto
era aplicar el conocimiento adquirido en los dias anteriores,
asi que, ya para otra ocasion se palicara esas ideas mas 
complejas.

Si alguien ve este codigo o para mi yo del futuro, no
olvides que a pesar de las complicaciones y los errores
persevera, toma un break no y replanteate lo que estas
haciendo, o tus ideas. Lo digo ya que yo tenia una idea
y al final para tener una version funcional y lista para
publicar, tuve que replantearme mi idea en base a los 
conocimientos que en este momento tengo, y no hay nada 
de malo en eso, algo si, a pesar de que hoy no se pudo,
no significa que luego no se pueda, siempre busca la manera 
de avanzar y creser. Asi que nos vemos otro dia con mas 
codigo 💻✨

Nota: “No es recomendable tener varios bucles en
un mismo bucle… al final provocará errores…”

Porque cada while necesita su propio break 
o condición de salida. Si olvidas uno, el 
programa se queda atrapado allí. Y si haces 
break en el bucle equivocado, el programa termina 
antes o sigue corriendo cuando no debería.

Solo hay que ser muy cuidadoso con los bucles. 😉✨

"""
