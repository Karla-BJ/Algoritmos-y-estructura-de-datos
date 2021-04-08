
listaNombres = ["Karla", "Arturo", "Lauras", "Juan"]
print ("Karla" in listaNombres)

encontro = falso
busqueda = "Karla"
for elemento in listaNombres:
    if elemento == busqueda:
        encontro = True

print (encontro)
print (listaNombres.index ("Karla"))
posicion = None
for i in range (len (listaNombres)):
    if listaNombres [i] == busqueda:
        posicion = i
print (posicion)
