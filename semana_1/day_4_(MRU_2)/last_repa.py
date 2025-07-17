#🧪 Reto Final del Día – MRU con Función return

""" 
📘 Enunciado:

1.Crea una función llamada calcular_distancia(v, t)

2.Que reciba dos parámetros:

*v: velocidad (en m/s)

*t: tiempo (en segundos)

3.Dentro de la función, devuelve la distancia con return

4.Luego:

*Pide los datos al usuario (input())

*Convierte los datos a float

*Llama a la función y guarda el resultado en una variable

*Imprime el resultado con un mensaje tipo pasteloso ✨
"""

#bienvenida
print("""
Hola Usuario ☺️🩵. Bienvenido a este programa que
te ayudara a encontrar la distancia en tus
ejercicios de MRU. Empecemos 🤓✨.
""")

#inicio y definicion de funcion
def calcu_d(v, t): #agregamos parametro v y t (datos de operacion)
    return (v * t) #ingresamos lo que hara la funcion en return

#conjunto de variables + inputs
v = float(input("Ingresa el valor de la velocidad 🤓🫨\n")) #type<'float'>
t = float(input("Ahora, ingresa el valor del tiempo 🤓🕰️\n")) #type<'float'>

#variable resultado
op_d = f"El resultado de la distancia del objeto es de {calcu_d(v, t)} metros 🤓☝️\n" #type<'float'>

#imprime el resultado y final
print(op_d)

""" 
Conclusiones:

Ya con este ejercicio me queda mas claro el como se usa,
y el funcionamiento del return en una funcion. Me gustaria 
acotar tambien algo para mi yo del futuro o cualquier
persona que llegue a leer esto, cuando le damos un 
parametro a una funcion, el parametro tiene que estar 
asociado a lo que vamos hacer, o a las variables que 
vas a declarar, por ejemplo:

El proposito de mi funcion era calcular la distancia,
asi que agregue los parametros v y t, que son los
datos que se usan para calcular la distancia, ya que 
si no agrego estos parametros es como si la funcion
no estuviera ligada al proposito del programa o de 
lo que quiero hacer. asi que hay que estar pendientes 
de eso.

En este ejercicio, hemos dado uso de todas las herramientas
y funciones que hemos aprendido hoy, como es el:

1.def
2.return
3.input()

Nota: usamos la funcion de tipo "float()" en las variables
v y t, ya que asi no limitamos al usuario a ingresar solo 
numeros enteros, y asi el programa es mas flexible.

Nos vemos la proxima con mas codigo. 🤓💻🩵✨
"""