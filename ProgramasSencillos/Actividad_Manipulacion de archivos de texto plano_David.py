#- - - ACTIVIDAD - - -
# Prueba de manipulación de archivos de texto plano


# ----------------------------------------------------------------
# Nombre del codigo: Manipulación de archivos de texto plano
# Objetivo / propósito: Manipular archivos de textos planos, probarlos y ver en que caso se rompe (siguiendo el orden dada en clase)
# Parámetros de entrada: Un texto largo
# Parámetros de salida: El archivo de texto
# Desarrolló: David Bojalil Abiti, 25-Septiembre-2022
#----------------------------------------------------------------

f = open("prueba.txt", "a")
f.write(" Mi visual studio esta roto ")
text = input("Escribe un texto: ")
f.write(text)
f.close()

p = open("prueba.txt","r")
print(p.read())
'''
- Las siguientes lineas dan error y no se pueden ocupar debido a que no se puede escribir cuando se abre un archivo en read :) -
text = input("Escribe un texto: ")
p.write(text) 

'''
p.close()




