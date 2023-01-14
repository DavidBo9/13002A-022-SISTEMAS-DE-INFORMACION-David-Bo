#- - - ACTIVIDAD - - -
# Encontrar la frecuencia de preposiciones en un texto


# ----------------------------------------------------------------
# Nombre del codigo: Frecuencia de preposiciones
# Objetivo / propósito: Encontrar la frecuencia de preposiciones en el texto
# Parámetros de entrada: Un texto largo
# Parámetros de salida: La frecuencia de 10 preposiciones
# Desarrolló: David Bojalil Abiti, 25-Septiembre-2022
#----------------------------------------------------------------
preposition = {'in':0, "by": 0, "from": 0, "to": 0, "off": 0, "at": 0, "into": 0, "through": 0, "on": 0, "ago": 0}

f = open("cuento.txt","r") 
p = (f.read()).lower()
a = p.split()

for line_number, line in enumerate(a, start=1):
    if line == 'in':
        preposition['in']+=1
    elif line == 'by':
        preposition['by']+=1
    elif line == 'from':
        preposition['from']+=1
    elif line == 'to':
        preposition['to']+=1
    elif line == 'off':
        preposition['off']+=1
    elif line == 'at':
        preposition['at']+=1
    elif line == 'into':
        preposition['into']+=1
    elif line == 'through':
        preposition['through']+=1
    elif line == 'on':
        preposition['on']+=1
    elif line == 'ago':
        preposition['ago']+=1
        
print("El contador de frecuencia preposiciones es el siguiente: ", preposition)
f.close()



