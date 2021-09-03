print ("Primer punto")
#Escriba un código en Python que calcule el área de una circunferencia a partir del radio preguntado al usuario

r= float (input ("Ingrese el radio de la circunferencia a la cual desea calcular el área : "))
area= 3.1416 * r**2

print (f"el área de la circunferencia es {area}")

#if r != 0:
#    print (area)
#else:
#    print ("Ingrese un valor válido para calcular el área")

print ("-"*60)
print ("Segundo punto")
#Escriba un código en Python que cuente la cantidad de números pares dada una lista de entrada

def contarPares (lista):
    pares= 0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            pares += 0

    return pares

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

contador= contarPares (numeros)

print (f"La cantidad de números pares es {contador}")

print ("-"*60)
print ("Tercer punto")
#Escriba un código en Python que cuente el número de veces que se repite un 
#nombre escogido por usted de una lista de entrada con múltiples nombres.

def contarKeylas (lista):
    keylas= 0

    for n in lista:
        if n == "Keyla":
            keylas += 1
        else:
            keylas += 0

    return keylas

nombres = ["Keyla", "Mónica", "Raúl", "Keyla", "Karen", "Alejandra", "Keyla", "Karla", "Skyler", "Keyla", "Sticker"]

contador= contarKeylas (nombres)

print (f"La cantidad de veces que se repite el nombre de Keyla es {contador}")

print ("-"*60)
print ("Cuarto punto")
#Escriba un código en Python que cuente el número de veces que se repite una letra dada una palabra de entrada 

palabra= input ("Ingresa una palabra para saber la cantidad de veces que se repite la letra A : ")

resultado = palabra.count("a")

print (f"La letra A se repite {resultado} veces")

print ("-"*60)
print ("Quinto punto")
#Escriba un código en Python que cuente el número de veces que se repiten cada una de las 5 vocales 
#en una palabra de entrada

palabra= input ("Ingresa una palabra para saber la cantidad de veces que se repiten las vocales : ")

resultadoA = palabra.count("a")
resultadoE = palabra.count("e")
resultadoI = palabra.count("i")
resultadoO = palabra.count("o")
resultadoU = palabra.count("u")

print (f"La letra A se repite {resultadoA}, la E se repite {resultadoE}, la I se repite {resultadoI}, la O se repite {resultadoO}, la U se repite {resultadoU} ")

print ("-"*60)
print ("Sexto punto")

edad= int (input ("Ingrese su edad : "))
comorbilidad= (input ("¿Tiene alguna comorbilidad : "))
reciente= (input ("¿Ha tenido covid los últimos tres meses? : "))

def definir_vacunacion (comorbilidad, reciente):
    vacuna=[]

    if comorbilidad == "si":
        comorbilidad == True
        vacuna.append (comorbilidad)
    else:
        comorbilidad == False

    if reciente == "no":
        reciente == False
        vacuna.append (reciente)
    else:
        reciente == True

    if vacuna == [True, False]:
        print ("Si cumple con las condiciones para vacunarse")
    else:
        print ("No cumple con las condiciones para vacunarse")

    return vacuna
    print (vacuna)


autorizacion= definir_vacunacion ()
