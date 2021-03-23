import time
import ordenamientoB as ob
import random as r
import OrdenamientoI as oi

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

#---InicioBurbuja---#
inicio = time.time()
#---Instrucciones---#
oi.ordenamientoInsercion(lista)
#---Delta---#
deltaOi = time.time() - inicio

#---InicioSort---#
inicio = time.time()
#---Instrucciones---#
listaCopia.sort()
#---Delta---#
deltaSort = time.time() - inicio

#---InicioSort---#
inicio = time.time()
#---Instrucciones---#
listaCopia.sort()
#---Delta---#
deltaSort = time.time() - inicio

print(deltaSort)
print (deltaOb)
print (deltaOi)
print(deltaSort >= deltaOb)
print(deltaSort >= deltaOi)

