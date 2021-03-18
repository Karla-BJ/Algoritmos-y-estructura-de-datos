#Fibonacci: 0,1,1,2,3,5,8,13,21

#----Preguntas----#
pregunta_numero = "ingrese un número entero : "
#----Mensajes error----#
error_entrada= "Entrada no válida"
#----Entradas----#
numero = None
while (numero == None):
    try:
        numero = int (input(pregunta_numero))
    except ValueError:
        print (error_entrada)
print (numero)

numeroAnterior = 0
numeroActual = 1

if (numero == 1):
    print (numeroActual)
elif (numero == 2):
    print(numeroActual)
else:
    for i in range (2, numero+1):
        print(i)
        aux = numeroAnterior
        numeroActual = numeroAnterior + numeroActual
        numeroAnterior = aux
        print (numeroActual)
    print ("salida", numeroActual)