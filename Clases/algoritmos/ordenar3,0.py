import time
import ordenamientoB as ob
import random as r

lista= []
for i in range (1200):
    lista.append (r.randint(1,10000))
listaCopia = lista.copy()

#---InicioBurbuja---#
inicio = time.time()
#---Instrucciones---#
ob.ordenamientoBurbuja(lista)
#---Delta---#
deltaOb = time.time() - inicio

#---InicioSort---#
inicio = time.time()
#---Instrucciones---#
listaCopia.sort()
#---Delta---#
deltaSort = time.time() - inicio

print(deltaSort)
print (deltaOb)
print(deltaSort >= deltaOb)
