def busquedaLineal(lista,encontrar):
    isInList= False
    for elemento in lista:
        if elemento == encontrar:
            isInList = True
    return isInList

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEncontrar = int (input("Ingrese un número : "))

print (busquedaLineal(listaEntrada, valorEncontrar))
import busquedaBi as bi
import time
import random as rd
listaEntrada = []
for i in range (10000):
    listaEntrada.append(rd.randint(1,100000))
encontrar = 59
listaEntrada.sort()
inicio = time.time()
busquedaLineal(listaEntrada,encontrar)
deltaLineal = time.time () - inicio
inicio = time.time ()
bi.busquedaBinaria(listaEntrada, encontrar)
deltaBunario = time.time () - inicio
print (deltaBunario, deltaLineal)
