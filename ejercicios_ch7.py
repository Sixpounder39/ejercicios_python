# Estos son los ejercicios del cap 7
# https://books.trinket.io/pfe/07-files.html

# 1. Escribe un programa para leer a través de un archivo e imprimir el contenido del fichero (línea por línea) todo en mayúsculas (fichero mbox-short)

fichero = open("mbox-short.txt", "r")

for i in fichero: 
    # En este caso también borro los saltos de línea que tiene
    print(i.rstrip().upper())

fichero.close()


# 2. Escribe un programa para leer a trabés del mismo archivo pero, que saque el promedio de todos los X-DSPAM-Confidence que se encuentren, esto aplicarlo en 
# mbox-short (0.750718518519) y m-box (0.894128046745)

# Realizo esta función para que pueda utilizarse con ambos ficheros

def dspam(fichero):
    suma = 0 # Realizará la suma de los datos encontrados
    num = 0 # Convertirá los números txt a float
    contador = 0 # Contador que indica cuántos elementos ha encontrado

    for i in fichero:   
        # Si encuentra coincidencia entonces realizará el proceso
        if not i.find("X-DSPAM-Confidence: "):
            #print("Si hay ", i.strip())    
            confidencia = i.find("X-DSPAM-Confidence: ")   # muestra en dónde encuentra el elemento 
            texto = i[confidencia:] # Se captura esa línea
            confidencia = texto.find(":") # se indica que encuentre el índice donde empieza el ":"
            texto = i[confidencia:].replace(":","").strip() # se pide iniciar desde ese índice y reemplazar el ":" por espacio, luego limpia todos los espacios
            num = float(texto) # se asigna como flotante lo que encontró (el número ya escombrado)
            suma = suma + num # se realiza la suma de los elementos
            contador = contador + 1 # se cuenta la cantidad de elementos
            #print(suma)
            #print("El contador es: ", contador)
    
    print("El promedio de X-DSPAM-Confidence en el fichero es de: ", str(suma/contador))

# Ejecuto el resultado del primer fichero

ficheroA = open("mbox-short.txt", "r")
dspam(ficheroA)
ficheroA.close()

# Ejecuto el resultado del segundo fichero

ficheroB = open("mbox.txt", "r")
dspam(ficheroB)
ficheroB.close()

# 3. Escribe un programa que lea un fichero e indique el total de líneas que tiene, que indique si no existe y que muestre un easter egg en caso de escribir "na na boo boo": "eres un punk!"


print("\n******************************")
fichero = input("Escribe el nombre del fichero que requieres encontrar: ")


if fichero == "na na boo boo":
    print("Eres un punk!")
else:

    try:
        f = open(fichero, "r")
        print("El fichero que mencionas sí existe: ", f)
        f.close()
    except Exception as e:
        print("Este fichero NO EXISTE, valida de nuevo")





