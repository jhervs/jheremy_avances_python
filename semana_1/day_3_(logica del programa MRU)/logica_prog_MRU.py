#Logica del Programa MRU (parte 1)

""" 
✅ Resumen rápido de tu misión para hoy:
🎯 Objetivo: Construir la primera versión funcional de tu Simulador de MRU

🧱 Estructura sugerida:

*Bienvenida y menú

*Input del usuario para elegir qué quiere calcular

*Pedir los dos valores necesarios

*Realizar el cálculo con la fórmula correspondiente

*Mostrar el resultado con f-string

*Dejar comentarios y explicaciones como siempre haces 💙
"""
again = "si" #type<str>

#bucle que condiciona al programa a iniciarse o no.
while again == "si":
    print("""
Hola usuario. Bienvenido a este programa intuitivo
simulador de MRU 🤓. Aqui te ayudaremos a solucionar
tu ejercicio de MRU, solo necesitamos que nos digas 
que operacion necesitas hacer y nos facilites los datos
que tengas. Empecemos. 💪✨\n
""")
    
#ingreso de operacion.
    user_op = (input("""
De acuerdo ¿Que operacion, vas a realizar hoy?

1. buscar "d"
2. buscar "v"
3. buscar "t"

Coloca la letra, d, v ó t, en base a lo que necesitas hacer.\n
""".lower())) 

#lower() usado para que la salida siempre sea minuscula.

    if user_op != "d":
        print("""
Nota: recuerda que si necesitas a bucar 
los datos, "v" y "t", en la division de la formula,
"d" siempre va arriba, asi que asegurate que 
el primer dato que ingreses sea "d" 
""")

#condicional que arroja una nota de recordatorio.


#ingreso de valores numericos type<'int'>.
    dato_1 = int(input("Ahora, ingresa el valor del primer dato que tengas.\n"))

    dato_2 = int(input("Muy bien, ahora ingresa el segundo valor ☺️\n"))

#variables operacionales (creo que agilizaria las condiciones de adelante).

    d =  dato_1 * dato_2 #type<'int'>

    v = dato_1 / dato_2 #type<'float'>

    t = dato_1 / dato_2 #type<'float'>

#inicio de condicionales y ejecucucion de ejercicio.
    if user_op == "d":
        print(f"\n El valor de la distancia recorrida es de {d} m ")
    elif user_op == "v":
        print(f"\n El valor de la velocidad del objeto en cuestion es de {v} m/s ")
    elif user_op == "t":
        print(f"\n El valor del tiempo del objeto es de {t} s ")
    else:
        print("Lo sentimos, el valor ingresado no es soportado 😵‍💫 ")

    again = input("""
Muy bien. ¿Ahora quieres calcular otro dato?

Si quieres seguir escribe "si" y si no hay mas nada que calcular
escribe "no"\n

""")

    if again == "no":
        print("""
Ha sido un placer calcular dato contigo,
si en otra ocasion quieres calcular mas datos
te ayudare con gusto.\n
""")

""" 
Bueno, les contare que fue lo que hice.
en este programa busque la manera que 
este fuera mas intuitivo, con lo que me 
refiero a esto es que este, a demas de 
que haga algo en base a las respuestas 
del usuario, tambien queria que este
se volviera a iniciar por medio de un bucle 
dandole asi una continuidad al programa.
esa ultima parte me costo un poco, pero
era algo que realmente queria hacer. En
el codigo fui poniendo comentarios cortos
para ir guiandome paso por paso, sobre lo que
hace cada parte de la estructura del codigo,
y asi poder orientarme mejor a la hora de querer 
editar o añadir algo. Use condicionales,
inputs, funciones de tipo, f-string para
concatenar cadenas con variable, while para
hacer el bucle y algunos operadores logicos 
y tambien matematicos.

En conclusion, es un programa simple, aun hay
maneras de mejorar el codigo, por ejemplo 
agregar un diccionario para que las variables
sean asociadas con la letra inicial de la operacion
("str") como tambien se podria usar definiciones 
pero eso ya son temas que aun no manejo, pero
que proximamente lo haremos si si. Y bueno, creo 
que esto es todo, en programa me esforce bastante para
que la idea de como queria que funcionara el programa,
pasara al codigo, creo haber logrado casi igualarla.
ya mas adelante mejoraremos el programa para que este
bien pulido y listo para el portafolio. 🤓💻🥹🩵✨

Nota: Cuando usamos un condicional while, tenemos 
que asegurarnos de que todo este bien estructurado
y organizado, a lo que me refiero es que, por ejemplo
en este ejercicio, el codigo tenia varias condiciones
y como el bucle while, fue lo ultimo que añadi, tuve que 
organizar el codigo haciendo que tanto las variables como
las condiciones esten adentro del bucle para que asi
funcione nuestro programa tal como queremos, asi que 
tanto para mi yo del futuro y por si alguien lee esto,
hay que estar mosquita con esto jeje 😉🩵✨. 
"""