lista= [2,25,34,65,8]
potenciador= lambda valor = 0 : valor **2
listaCuadrados = list (map(potenciador, lista))
print (potenciador(4))
print (listaCuadrados)

lista3 = [2,24,5,45,122,3]
listaCuadrados2 = list (map(potenciador,lista3))
print (listaCuadrados2)

retornarListaCuadrados = lambda listaEntrada = [] : list(map(potenciador, listaEntrada))
lista4 = [2,34,35,2,1,4]
listaCuadrados4= retornarListaCuadrados (lista4)
print (listaCuadrados4)

n=2
restarN = lambda valor : valor - n
print (restarN (3))
restarNlista = list (map(restarN,lista4))
print (restarNlista)

#Normalizar

mayor = max(lista4)
dividir= lambda valor = 0 : valor/mayor 
listaNormalizada = list (map(dividir,lista4))
print (listaNormalizada)

#IMC
pesos = [56,77,85,46,89]
estaturas= [1.25,1.56,1.89,2.00,1.58]

imc = lambda peso = 0, estatura = 1 : peso / estatura**2
imcListas= list (map(imc,pesos,estaturas))
print (imcListas)

#Área de un triangulo
bases = [2,3,4,5,7,9]
alturas= [23,45,67,84,45,67]
divisores = [2,2,2,2,2,2]
calcularAreaTriangulo = lambda base = 0 , altura = 0, divisores = 1: base*altura/divisores
listaAreasTriangulos= list (map (calcularAreaTriangulo, bases, alturas, divisores))
print (listaAreasTriangulos)
print (sum(bases))

#funciones reduce
from functools import reduce
sumarElementos = lambda acumulado= 0, elemento = 0 : acumulado + elemento
sumar= reduce (sumarElementos, bases)
print (sumar)

multiplicarElementos = lambda acumulado = 0, elemento = 1 : acumulado * elemento
multiplicar = reduce (multiplicarElementos, bases)
print (multiplicar)

print (multiplicar/sumar)
