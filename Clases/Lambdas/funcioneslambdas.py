def linedesing (cantidad):
    print ("♥"*cantidad)

def sumar (a,b):
    suma= a+b
    return suma
def restar (a,b):
    resta= a-b
    return resta
def multiplicar (a,b):
    multiplicacion= a*b
    return multiplicacion
def dividir (a,b):
    divicion= a/b
    return divicion

def calculadora (funcion, a,b ):
    return funcion (a,b)


linedesing (30)
print ("hola a todos")
linedesing(20)
print (sumar(2,6))
linedesing(20)
print (restar(2,6))
linedesing(20)
print (multiplicar(100,87))
linedesing(20)
print (dividir(100,87))
linedesing(20)
print (calculadora (sumar, 100,87))
linedesing(20)

print ("Ahora lo mismo pero con lambdas")

linedesingLambda= lambda cantidad=60 : print ("♥"*cantidad)
linedesingLambda()
sumar2 = lambda a = 0 , b = 0 : a+b
print (sumar2(4,5))
linedesingLambda()
restar2= lambda a = 0 , b = 0 : a - b
print (restar2(53,57))
linedesingLambda ()
multiplicar2= lambda a = 0 , b = 0 : a * b
print ( multiplicar2(2,3))
linedesingLambda ()
dividir2= lambda a = 0 , b = 0 : a / b
print (dividir2 (5,2))
linedesingLambda ()
calculadora2= lambda func= restar2, a = 0 , b = 0 : func(a,b)
print (calculadora2(multiplicar2, 68,63))
linedesingLambda ()

listaEdades1= [18,12,14,13,12,20]
listaEdades2= [18,25,46,75,90,23]

lambdamax = lambda x = [], y = [] : print (max(x), max (y))
lambdamax (listaEdades1, listaEdades2)

mayorEdad= lambda edad = 0 : edad >= 18
print (mayorEdad(14))
print (mayorEdad(19))
mayores = list (filter(mayorEdad, listaEdades1))
print (mayores)

