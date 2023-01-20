# Basado en curso de estructura de datos Coursera CAP 6

#############  CONCATENACIÓN DE CADENAS

# Cuando se usa el "+" aplicado a las cadenas, significa concatenación

a = "Hola"
b = a + "mundo"
print(b)

# imprime "Holamundo"

# Si se requiere un espacio, se debe indicar de manera explícita

c = a + " " + "mundo"
print(c)

# imprime "Hola mundo"

########### IN COMO OPERADOR LÓGICO

# IN puede ser utilizado par arevisar si una cadena existe dentro de otra
# Retorna cierto o falso y puede ser utilizada en un IF

fruta = "platano"
print("n" in fruta)
# Imprime True

print("m" in fruta)
# Imprime False

print("plata" in fruta)
#Imprime True

if ("t" in fruta):
    print("Hay una t en fruta!")

########### Comparación de cadenas

#Se puede revisar qué palabra va antes de otra recordando que las mayúsuculas
#tienen un orden de prioridad mayor a las minúsculas, quiere decir que
#pedro tiene menor peso que Tania, pero Pedro tiene mayor peso que Tania

palabra = "Sandía"

if palabra == "plátano":
    print("OK, tenemos plátanos")

if palabra < "plátano":
    print("Tu palabra " + palabra + " está antes que plátano")

elif palabra > "plátano":
    print("Tu palabra " + palabra + " está después que plátano")

else:
    print("OK, hay tenemos plátanos")

############ MÉTODOS QUE SE PUEDEN APLICAR A LAS CADENAS

cosa = "Hola mundo"

# podemos ver de que tipo es, en este caso de clase STR

print(type(cosa))
# Imprime: <class 'str'>

# podemos ver qué métodos podemos emplear a este tipo de dato, como convertir
# todo en mayúsuculas o minúsulas, unir, saber si son números, etc.

print(dir(cosa))
"""
 Imprime: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
  'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
   'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
 """

# Un ejemplo de aplicación para convertir de mayúsculas a minúsculas

cadena = "QUE TAL cómo ESTÁN todoS"
print(cadena) # imprime la cadena tal como se ingresa

print(cadena.lower()) # lower(), pasa todos los caracteres a minúsculas

############ BÚSQUEDA EN UNA CADENA

# Podemos utilizar find() para buscar una subcadena en otra cadena
# find() indica la primer coincidencia en la cadena, si no encuentra nada, retorna -1

# P L A T A N O
# 0 1 2 3 4 5 6 

fruta = "plátano"
posicion = fruta.find("ta")
print(posicion)

# Imprime 3, que es el índice donde comienza y encuentra dicha subcadena

posicion_inexistente = fruta.find("za")
print(posicion_inexistente)

# Imprime -1 porque no existe coincidencia alguna


############### BUSCAR Y REEMPLAZAR

# replace() es una función que busca y reemplaza una palabra, esto se aplica
# a todas las coincidencias que encuentre en la cadena

saludo = "Hola señor Calamardo"
nsaludo = saludo.replace("Calamardo", "Patricio")
print(nsaludo)
# Imprime: Hola señor Patricio

nsaludo = saludo.replace("o", "X")
print(nsaludo)
# Imprime: HXla señXr CalamardX

############# ESPACIOS EN BLANCO

# Puedes remover espacios al final o inicio de una cadena
# lstrip() remueve a la izquieda, rstrip() a la derecha
# strip() remueve a ambos lados

saludo = "            Hola señor Calamardo   "
print(saludo.lstrip())
# Borra los espacios a la izquierda de la cadena

print(saludo.rstrip())
# Borra los espacios a la derecha de la cadena

print(saludo.strip())
# Borra los espacios a la izquierda y derecha

############# PREFIJOS

# startswith() nos retorna cierto o falso en caso de que una cadena coincida
# con el inicio de alguna otra subcadena, por ejemplo:

linea = "Por favor, ten un buen día"
print(linea.startswith("Por favor"))
# Imprime "True"

print(linea.startswith("p"))
# Imprime "False", porque no empieza con "p" minúscula


############# ANALIZANDO Y EXTRAYENDO

# En este ejemplo, obtendremos el dominio de un correo electrónico en una cadena

dato = "From prueba@test.com Sat Jan 5 09:14:16"
inicio = dato.find("@") # buscamos la posición inicial tomando como referencia el arroba
print(inicio) #devolverá 11

final = dato.find(" ", inicio) # buscamos el primer espacio que vea desde inicio
print(final)

dominio = dato[inicio+1:final] # obtenemos la cadena deseada indicando de dónde a dónde
print(dominio) # Imprime test.com


############## EJERCICIO

# Usa find y sustrae la porción de cadena después de los dos puntos y usa la funcion float para convertr el número a coma flotante

cadena = 'X-DSPAM-Confidence: 0.8475'

# Para este caso, voy a ubicar la posición de los dos puntos

posicion = cadena.find(":")
print(posicion)

# tomo toda la cadena desde ahi hasta que termina y limpio espacios en blanco

numero = cadena[posicion+1:].strip()
print("El número en cadena es: " + numero)

# Ahora convierto a flotante

numero = float(numero)
# Como el número ya es flotante, tengo que convertirlo en str para concatenarlo e imprimirlo en pantalla
print("El número en cadena de flotante a str es " + str(numero))
