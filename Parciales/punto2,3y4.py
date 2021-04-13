#Primer punto#
#La ecuación es: 

#Segundo punto#

#Algoritmo a: LA SUCESIÓN ES 1/2^n-1, n es la posición# 
listaEntrada= [1,1/2,1/4,1/8,1/16]
preguntaNúmero= int(input("Ingrese un número correspondiente a el término enésimo que quiera saber de la sucesión : "))
error_entrada= "Entrada no válida"

if (preguntaNúmero == 0):
    print (error_entrada)
else:
        numeroActual = 1/2** (preguntaNúmero-1)
        print (numeroActual)


#Algoritmo b: LA SUCESIÓN ES 2n+1, n es la posición# 
listaEntrada2= [3,5,7,9,11]
preguntaNúmero= int(input("Ingrese un número correspondiente a el término enésimo que quiera saber de la sucesión : "))

if (preguntaNúmero == 0):
    print (error_entrada)
else:
        numeroActual = 2*preguntaNúmero+1
        print (numeroActual)

#CUARTO PUNTO#

def contarPalabrasV1(parrafo):
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
    return dictPalabrasOcurrencias

def contarPalabrasV2(parrafo):
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = 0
        for i in range (len(listaPalabras)):
            if palabra == listaPalabras[i]:
                dictPalabrasOcurrencias[palabra] += 1
    return dictPalabrasOcurrencias

import time

parrafo=''' (Tiempo para mirar un árbol, un farol
Para andar por el filo del descanso
Para pensar qué bien hoy no es invierno
Para morir un poco y nacer enseguida
Y para darme cuenta
Y para darme cuerda
Preciso tiempo el necesario
Para chapotear unas horas en la vida
Y para investigar por qué estoy triste
Y acostumbrarme a mi esqueleto antiguo)'''

inicio1= time.time ()
contarPalabrasV1(parrafo)
deltaV1= time.time()-inicio1
inicio2= time.time()
contarPalabrasV2(parrafo) 
deltav2= time.time()-inicio2
print(deltaV1,deltav2)

#Aunque el resultado de la comparación de los tiempos diera igual, 
#a partir de la estructura del código, podemos concluir que la función 
# más óptima es la segunda"