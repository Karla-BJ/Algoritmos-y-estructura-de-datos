#Ordenamiento por burbuja
def ordenamientoBurbuja (lista= []):
    sizeList = len (lista)
    for i in range (sizeList):
        for j in range (sizeList-1):    
            if (lista [j]>lista[j+1]):
                lista [j+1], lista [j] = lista[j], lista[j+1]
    return lista

