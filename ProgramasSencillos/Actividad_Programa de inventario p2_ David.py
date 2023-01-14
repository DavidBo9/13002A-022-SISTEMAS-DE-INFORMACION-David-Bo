#- - - ACTIVIDAD - - -
# Crear un programa de suministros en donde se pueda
# registrar, mostrar, actualizar, frecuencia, encontrar total y buscar los datos 
# almacenados

# ----------------------------------------------------------------
# Nombre del programa: programa de suministros
# Objetivo / propósito: registrar, mostrar, actualizar, frecuencia, encontrar total y buscar datos
# Parámetros de entrada: diccionario de suministros
# Parámetros de salida: registrar, mostrar o buscar
# Lenguaje: Python
# Desarrolló: David Bojalil Abiti, 26-Septiembre-2022
#----------------------------------------------------------------

suministros = {
    1:{
        'cantidad':5,
        'nombre':'platos',
        'precio':10.0
    },
    2:{
        'cantidad':5,
        'nombre':'vasos',
        'precio':10.0

    }
}

# ----------------------------------------------------------------
# Nombre de la función: Menu
# Objetivo / propósito: Poner un menu de opciones para que el usuario pueda elegir la opcion
# Parámetros de entrada: N/A
# Parámetros de salida: N/A
# Desarrolló: David Bojalil Abiti, 26-Septiembre-2022
#----------------------------------------------------------------
def menu():
    print("Bienvenido al menu de suministros, ¿que te gustaria hacer?")
    print("--- [Menu] ---")
    print("[1] Registrar suministro")
    print("[2] Buscar suministro")
    print("[3] Mostrar todo")
    print("[4] Modificar dato")
    print("[5] Mostrar total")
    print("[6] Buscar tendencia")
    print("[7] Exportar datos")
    print("[8] Importar datos")
    print("[0] Salir")
    pass
menu()

# ----------------------------------------------------------------
# Nombre de la función: Menu
# Objetivo / propósito: Poner un menu de opciones para la funcion de modificar 
# Parámetros de entrada: N/A
# Parámetros de salida: N/A
# Desarrolló: David Bojalil Abiti, 28-Septiembre-2022
#----------------------------------------------------------------
def menumodificar():
    print(" ")
    print("--- [Menu modificación] ---")
    print("[1] Cambiar cantidad")
    print("[2] Cambiar nombre")
    print("[3] Cambiar precio")
    print("[0] Salir")
    pass

# ----------------------------------------------------------------
# Nombre de la función: Registrar suministro
# Objetivo / propósito: Registrar suministro en el diccionario
# Parámetros de entrada: diccionario de suministros
# Parámetros de salida: Registro de suministro
# Desarrolló: David Bojalil Abiti, 26-Septiembre-2022
#----------------------------------------------------------------
def opc1():
    i = (len(suministros)+1)
    cantidad = int(input("Cual es la cantidad a insertar: "))
    suministros[i] = {1:{
        'cantidad':5,
        'nombre':'platos',
        'precio':10.0
    },
    2:{
        'cantidad':5,
        'nombre':'vasos',
        'precio':10.0

    }} 
    suministros[i]['cantidad'] = cantidad
    nombre = (input("Cual es el nombre a insertar: "))
    suministros[i]['nombre'] = nombre
    precio = float(input("Cual es el precio a insertar: "))
    suministros[i]['precio'] = precio
    pass

# ----------------------------------------------------------------
# Nombre de la función: Buscar suministro
# Objetivo / propósito: Buscar suministro en el diccionario
# Parámetros de entrada: Diccionario de suministros
# Parámetros de salida: Suministro buscado
# Desarrolló: David Bojalil Abiti, 26-Septiembre-2022
#----------------------------------------------------------------
def opc2():
    i = int(input("¿Que producto quieres buscar: "))
    if i <= len(suministros):
        print(f"Tienes {suministros[i]['cantidad']} {suministros[i]['nombre']} con un precio de {suministros[i]['precio']}")
        return i
    else:
        print("Error, no existe este producto")
    pass

# ----------------------------------------------------------------
# Nombre de la función: Mostrar suministros
# Objetivo / propósito: Mostrar todos los suministros
# Parámetros de entrada: diccionario de suministros
# Parámetros de salida: todos los suministros registrados en el diccionario
# Desarrolló: David Bojalil Abiti, 26-Septiembre-2022
#----------------------------------------------------------------
def opc3():
    i = 1
    for i in range (len(suministros)):
        print(f"Tienes {suministros[i+1]['cantidad']} {suministros[i+1]['nombre']} con un precio de {suministros[i+1]['precio']}")
    pass

# ----------------------------------------------------------------
# Nombre de la función: Modificar suministro
# Objetivo / propósito: Modificar algun dato de los suministros
# Parámetros de entrada: ID del suministro a cambiar
# Parámetros de salida: Suministro actualizado
# Desarrolló: David Bojalil Abiti, 28-Septiembre-2022
#----------------------------------------------------------------
def opc4(a):
    menumodificar()
    opc = int(input("Seleccione alguna opción: "))
    while opc != 0:
        if (opc == 1):
            cantidad = int(input("Cual es la cantidad a insertar: "))
            suministros[a]['cantidad'] = cantidad
        elif (opc == 2):
            nombre = (input("Cual es el nombre a insertar: "))
            suministros[a]['nombre'] = nombre
        elif (opc == 3):
            precio = float(input("Cual es el precio a insertar: "))
            suministros[a]['precio'] = precio
        else:
            print("Opción invalida")
        print(f"Tienes {suministros[a]['cantidad']} {suministros[a]['nombre']} con un precio de {suministros[a]['precio']}")
        menumodificar()
        opc = int(input("Seleccione alguna opción: "))
    pass

# ----------------------------------------------------------------
# Nombre de la función: Mostrar total
# Objetivo / propósito: Mostrar el total de datos de los suministros
# Parámetros de entrada: diccionario de suministros
# Parámetros de salida: Mostrar total de precio x producto, total de productos y total de ingresos
# Desarrolló: David Bojalil Abiti, 28-Septiembre-2022
#----------------------------------------------------------------
def opc5():
    i = 1
    total2 = 0
    cantidad = 0
    cantidadtotal = 0
    precio = 0
    total1 = 0
    for i in range(len(suministros)):
        cantidad = suministros[i+1]['cantidad']
        cantidadtotal = cantidad + cantidadtotal
        precio = suministros[i+1]['precio']
        total1 = cantidad * precio
        print(f"Tienes un total de precio de {suministros[i+1]['nombre']} de", total1)
        total2 = total1+total2
    print("Tienes un total de productos de:", cantidadtotal)
    print("El total de ingresos es de: ", total2)

# ----------------------------------------------------------------
# Nombre de la función: Mostrar tendencia
# Objetivo / propósito: Mostrar la tendencia de los datos
# Parámetros de entrada: diccionario de suministros
# Parámetros de salida: Suministro de: mayor y menor cantidad, mayor y menor precio
# Desarrolló: David Bojalil Abiti, 28-Septiembre-2022
#----------------------------------------------------------------
def opc6():
    i = 1
    cantidad3 = 10000
    cantidad2 = 0
    precio2 = 0
    precio3 = 10000
    for i in range(len(suministros)):
        cantidad = suministros[i+1]['cantidad']
        precio = suministros[i+1]['precio']
        if (precio > precio2):
            precio2 = precio
            mayorp = i+1
        elif (precio < precio3):
            precio3 = precio
            menorp = i+1
        if (cantidad > cantidad2):
            cantidad2 = cantidad
            mayorc = i+1
        elif (cantidad < cantidad3):
            cantidad3 = cantidad
            menorc = i+1
    print(f"Producto de mayor precio: {suministros[mayorp]['nombre']}")
    print(f"Producto de menor precio: {suministros[menorp]['nombre']}")
    print(f"Producto de mayor cantidad: {suministros[mayorc]['nombre']}")
    print(f"Producto de menor cantidad: {suministros[menorc]['nombre']}")
    pass

# ----------------------------------------------------------------
# Nombre de la función: Exportar datos
# Objetivo / propósito: Exportar los datos a un archivo de texto
# Parámetros de entrada: diccionario de suministros
# Parámetros de salida: N/A
# Desarrolló: David Bojalil Abiti, 3-Octubre-2022
#----------------------------------------------------------------
def opc7():
    f = open('datos.txt', 'w')
    f.write(str(suministros))
    f.close()
    pass

'''
f = open('datos.txt', 'w')
for key, value in suministros.items():
    f.write((key,value))
f.close()

Referencia: DevEnum.com

------------------------

import json
with open('datos.txt', 'w') as f:
    f.write(json.dumps(suministros))
    
Referencia: GeeksForGeeks
'''


# ----------------------------------------------------------------
# Nombre de la función: Importar datos
# Objetivo / propósito: Importar los datos a un archivo de texto
# Parámetros de entrada: Archivo de texto
# Parámetros de salida: Diccionario con los datos del archivo de texto
# Desarrolló: David Bojalil Abiti, 3-Octubre-2022
#----------------------------------------------------------------
def opc8():
    f = open('datos.txt', 'r')
    d = f.readlines().split('\n')
    
    pass

#Notas sobres posibles funciones encontradas: pickle.dump, pickle.loads, self.whip, json.loads, ast.literal_eval



opc = int(input("Seleccione alguna opción: "))
while opc != 0:
    if (opc == 1):
        opc1()
    elif(opc == 2):
        opc2()
    elif(opc == 3):
        opc3()
    elif(opc == 4):
        a = opc2()
        opc4(a)
    elif(opc == 5):
        opc5()
    elif(opc == 6):
        opc6()
    elif(opc == 7):
        opc7()
    elif(opc == 8):
        opc8()
    else:
        print("Opción invalida")
    print()
    menu()
    opc = int(input("Seleccione alguna opción: "))
print("¡Adios! ")

