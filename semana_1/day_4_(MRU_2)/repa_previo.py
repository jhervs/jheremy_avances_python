
#🧪 Ejercicio 1 y 2: try-except, docstring

"""
📋 Objetivo: Aprender a capturar errores 
cuando el usuario mete datos incorrectos.

# 🧠 Enunciado:
# Escribe un programa que le pida al usuario un número.
# Si el usuario escribe algo que no es un número, 
el programa debe mostrar un mensaje de error bonito
# y luego seguir preguntando hasta que lo escriba bien.

# 👉 Pista:
# Usa un bucle `while` con `try-except` dentro.

"""

""" 
programa: Suma facil 🤓
Autor: Jheremy 💻🩵
Fecha: 07/07/25

Introduccion: El programa "Suma facil" consiste en resolver sumas,
el usuario ingresa los datos, los resuelve y entrega el resultado. 🤓
"""


#inicia bienvenida y pregunta de inicio.
welcome = (input("""

Hola usuario bienvenido a tu programa de sumas. 🤓💻

¿Vas a querer hacer operaciones hoy?

Escribe "si" o "no" para comenzar o no. ☺️ 🩵\n
""".lower()))

#inicia bucle, condiciones y detectamos errores

while welcome == "si": #inicio y bucle val_1
    try: #detectamos errores
        val_1 = float(input("Ingresa el primer valor. ☺️\n")) #type<'float'>
    except ValueError: #lanza mensaje de error
        print("Oops! El valor ingresado no es valido, intente otra vez 😅\n")
    else: #empieza bucle val_2
        val_2 = False #type<'bool'>
        while val_2 is False:
            try: #detectamos erroes
                val_2 = float(input("Ahora el segundo valor. 🤓\n"))
            except ValueError: #lanza mensaje de error
                print("Oops! El valor ingresado no es valido, intente otra vez 😅\n")
        else: #inicio de operaciones
            op_suma = val_1 + val_2 #variable operacional. type<'bool'>
            print(f"El resultado de la suma es {op_suma} 🤓✨")
            #inicio de condiciones (end or again)
            again = input("""
            Ahora ¿Quieres seguir con otra operacion? 🤔
            
            Ingresa "si" para seguir, o "no" para concluir.☺️\n
            """.lower())
            if again != "no":
                print("Sigamos con la proxima operacion. 🤓✨")
            else:
                print("Ha sido un gusto hacer calulos contigo ☺️, hasta la proxima. 🤓 🩵")
            break #final del programa
else: #cierre del programa (inicio)
    print("Ha sido un placer tenerte por aqui, sera en otra ocasion 🥹 🩵")


"""
Bueno, este programa me llevo un poco de tiempo ya que 
aplique cosas nuevas que no habia usado antes, como el,
try-except, y tambien un uso mas complejo del while.

Al principio no sabia muy bien como hacerlo, y cometi 
algunos errores por omision, como fueron el omitir un else
despues de armar un try-except. Tambien errores en el 
posisionamiento de cada parte del codigo, ya que 
como tengo varios bucles como tambien condiciones, cada
uno debe de ir de acuerdo al espacio correspomdiente.
Algo tambien que debo de acordarme es que cuando 
por ejemplo hago un while con un dato tipo bool,
tengo que usar los operadores logicos como son:
'!=' ; == ; is ... etc

algunas cosas que capas me dejaron dudas fue que en 
una parte del codigo, tuve que  usar un "is"
pero creo que la razon de eso es que antes habia 
declarado una variable con el mismo valor que le 
estaba entregando al while, por lo que tenia que 
porner si este es x cosas, se ejecuta el bucle.
aun que me queda confuso ya que siento que con un "=="
podria funcionar, mi conclusion de esto fue que, como
era un dato bool (False) en ese caso se usa is o not,
creo que esos son los operadores que se usan en estos casos.

Conclusion: En este programa podras ver el funcionamiento
de los bucles junto con, condicionales, algunos operadores 
varios como, operadores logicos como numericos, y tambien
algunos input para hacer mas interactivo el programa.
El proposito de este programa es la resolucion de sumas,
pidiendole los datos al usuario, y en base a sus respuesta
el programa responde de segun las condiciones integradas.

nota: Tuve un problemita con el segundo try-except,
era que el programa lo omitia, la solucion de esto
fue hacer bucles separados, uno en el valor 1 y otro 
en el valor 2. para que asi, una vez el usuario
ingresara los datos correctamente en el val_1
pasara al valor 2, cosa que no pasaba estando 
los dos en un mismo while, ya que directamente al
fallar uno, el programa se cortaba y volvia a iniciar
el bucle desde el principio omitiendo el segundo valor.
Asi el programa tiene una susecion y se ve mas natural.
hasta la proxima 🤓🩵💻✨
"""
