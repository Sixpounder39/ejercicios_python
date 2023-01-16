# Basado en curso de estructura de datos Coursera CAP 6

################## CADENAS Y TIPO DE DATOS

# Un string o cadena, es una secuencia de caracteres

print("Hola mundo!")

# Se escribe entre comillas y el símbolo "+" las concatena

str1 = "Hola"
str2 = "Mundo!"

cadena = str1 + " " + str2

print(cadena)

# Cuando una cadena contine numeros, sigue siendo una cadena

str3 = "123"

# Se pueden convertir numeros a cadena usando int()

x = int(str3) + 1

print(x)

# Salidas:

"""
Hola mundo!
Hola Mundo!
124

"""
################## LEYENDO Y CONVIRTIENDO

# Es preferible leer datos usando cadenas y luego convertirlos al dato que necesitemos
# Este nos da mayor control sobre situaciones de error o datos de entrada incorrectos


name = input("Ingresa tu nombre: ")
print(name)

# Números utilizados como entrada deben ser convertidos desde cadena

manzana = input("Ingresa número: ")
x = int(manzana) - 10

print(x)

################# BUSCAR DENTRO DE CADENAS

# Una cadena de caracteres múltiples tiene datos indexables dentro de ella

# A U T O M O V I L
# 0 1 2 3 4 5 6 7 8

# Podemos obtener cualquier caracter simple en una cadena usando un índice especifico dentro de corchetes

transporte = "automovil"
letra = transporte[2]
print(letra)

# Imprimirá "t"

# El valor del índice debe ser un entero y comienzan con cero

letra = transporte[0]
print(letra)

# Imprimirá "a"

# El índice puede ser una expresión que será computada

x = 3
w = transporte[x-2]
print(w)

# Imprimirá "u"

############# LONGITUD DE UNA CADENA

# Podemos usar la función len() que devuelve la cantidad de caracteres de la cadena

transporte = "metrobus"
x = len(transporte)
print(x)

# Imprimirá "8"

####### RECORRIDO EN LA CADENA

"""
Usando WHILE y una variable de iteración, podemos contruir un loop indefinido para
mirar cada una de las letras de la cadena en una cadena individual
"""

fruta = "platano"
index = 0
z =""


while index < len(fruta):
    z = fruta[index]
    print(index, z)
    index = index + 1

"""
Imprime:

0 p
1 l
2 a
3 t
4 a
5 n
6 o


"""
# Usando FOR podemos emplear un loop definido que es mucho más elegante

fruta = "platano"

for x in fruta:
    print(x)

"""
Imprime:

p
l
a
t
a
n
o


"""

################# LOOP Y CONTEO
"""
Este es un loop simple que itera cada letra de una cadena y cuenta
el número de veces que el loop encuentra la letra "a"
"""

palabra = "camaronera"
contador = 0

for x in palabra:
    if x == "a":
        contador = contador +1
print(contador) 

# Imprimirá "3"

############## SECCIONANDO CADENAS PT1

"""
Podemos mirar cualquier sección continua de una cadena utilizando los
dos puntos como operador. El primer número es el inicio en la cadena y el
segundo número el final, teniendo en cuenta que el final no se incluirá en
la sección realizada. Si el segundo número sobrepasa el total de caracteres consecuentes
entonces se detendrá al final de la cadena aunque tenga menos

"""
# M O N T Y   P Y T H O N
# 0 1 2 3 4 5 6 7 8 9 10 11

s = "Monty Python"
print(s[0:4])

# Imprime: Mont 

print(s[6:7])

# Imprime: P

print(s[6:20])

# Imprime: Python

################  SECCIONANDO CADENAS PT2

"""
Si no colocamos un número en el rango de la cadena a seccionar, ya sea al 
inicio o al ginal, se asume que se comienza desde el inicio o final respectivamente
"""

# M O N T Y   P Y T H O N
# 0 1 2 3 4 5 6 7 8 9 10 11

s = "Monty Python"

print(s[:2])

# Imprime: Mo

print(s[8:])

# Imprime: Thon

print(s[:])

# Imprime: Monty Python





