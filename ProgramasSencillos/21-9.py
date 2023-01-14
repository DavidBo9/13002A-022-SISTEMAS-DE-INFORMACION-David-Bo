f = open("cuento.txt", "r")

'''print(f.read())

#f.write("Merequetengue")

f = open("cuento.txt", "a")
text = input("Ingrese la cosa: ")

f.write(text)'''

d = {'de':0, 'a':0, 'con':0, 'contra':0, 'sin':0, 'hacia':0, 'desde':0, 'durante':0, 'en':0,'entre':0}

contenido = f.read().split()

for x in contenido:
	if x == 'de':
		d['de']+=1

	elif x == 'a':
		d['a']+=1

	elif x == 'con':
		d['con']+=1

	elif x == 'contra':
		d['contra']+=1

	elif x == 'sin':
		d['sin']+=1

	elif x == 'hacia':
		d['hacia']+=1

	elif x == 'desde':
		d['desde']+=1

	elif x == 'durante':
		d['durante']+=1

	elif x == 'en':
		d['en']+=1

	elif x == 'entre':
		d['entre']+=1

print(d)	
