#Punto 1#
print ("Punto 1")
print ("A continuación se muestran datos de los pacientes tratados en la ciudad de Medellín correspondientes cada mes del año 2020")
print ("-"*30)
import pandas as pd
dicPatientsPerYear= {}
dicPatientsPerYear ["Enero"] = 32121
dicPatientsPerYear ["Febrero"] = 14564
dicPatientsPerYear ["Marzo"] = 65465
dicPatientsPerYear ["Abril"] = 85202
dicPatientsPerYear ["Mayo"] = 93213
dicPatientsPerYear ["Junio"] = 100231
dicPatientsPerYear ["Julio"] = 120213
dicPatientsPerYear ["Agosto"] = 65421
dicPatientsPerYear ["Septiembre"] = 46546
dicPatientsPerYear ["Octubre"] = 46547
dicPatientsPerYear ["Noviembre"] = 84651
dicPatientsPerYear ["Diciembre"] = 140521
seriePatientsPerYear= pd. Series (dicPatientsPerYear)
print (seriePatientsPerYear)

print ("-"*130)

#Punto 2
print ("Punto 2")
print ("A continuación se muestran datos de los pacientes tratados en la ciudad de Medellín correspondientes a cada trimestre del año 2020")
print ("-"*30)
dicPatientsThreeMonth= {}
dicPatientsThreeMonth ["1er Trimestre"] = sum (seriePatientsPerYear[ "Enero":"Marzo"])
dicPatientsThreeMonth ["2do Trimestre"] = sum (seriePatientsPerYear[ "Abril":"Junio"])
dicPatientsThreeMonth ["3er Trimestre"] = sum (seriePatientsPerYear[ "Julio":"Septiembre"])
dicPatientsThreeMonth ["4to Trimestre"] = sum (seriePatientsPerYear[ "Octubre":"Diciembre"])
seriePatientsThreeMonth= pd. Series(dicPatientsThreeMonth)
print (seriePatientsThreeMonth)
print ("la suma total del año es igual a: ")
print ( sum(seriePatientsPerYear))

print ("-"*130)

#Punto 3
print ("Punto 3")
print ("A continuación se muestra el promedio de los pacientes tratados en la ciudad de Medellín correspondientes al año 2020")
print ("-"*30)
from functools import reduce
patientsList= [32121, 14564, 65465, 85202, 93213, 100231, 120213, 65421, 46546, 46547, 84651, 140521 ]
sumador= lambda acumulado = 0, elemento= 0: acumulado + elemento
promedio= reduce (sumador,patientsList)/len(patientsList)
print (f"el promedio de pacientes atendidos es igual a {promedio}")

print ("-"*130)

#Punto 4
print ("Punto 4")
print ("A continuación se muestra una tabla correspondiente a las enfermedades en Bogotá distribuidas durante el primer semestre del 2020")

print ("-"*30)

dicEnfermedadesBogota= {
    "Enfermedad General": [32121,14564,65465,85202,93213,100231],
    "COVID-19": [0,0,223,3453,4543,43643],
    "Traumatismos": [6545,43243,67657,435435,345345,43543],
    "Cáncer": [6541,4334,4323,34545,5454,7675]
} 
listaMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
dataFrameEnfermedadesBogota = pd.DataFrame(dicEnfermedadesBogota, index= listaMeses)
print (dataFrameEnfermedadesBogota)

print ("-"*130)

#Punto 5
print ("Punto 5")
print ("A continuación se muestra el promedio de los pacientes por COVID-19 durante los meses Abril, Mayo y Junio")
print ("-"*30)
from functools import reduce
COVIDList= [0, 0, 223, 3453, 4543, 43643]
sumador= lambda acumulado = 0, elemento= 0: acumulado + elemento
promedio= reduce (sumador,COVIDList)/len(COVIDList)
print (f"el promedio de pacientes atendidos es igual a {promedio}")

print ("-"*130)


#Punto 6
print ("Punto 6")
print ("A continuación se muestra el promedio de los pacientes por traumatismos y cáncer durante los meses Enero, Febrero y Marzo")
print ("-"*30)

print (dataFrameEnfermedadesBogota["Enero":"Marzo"][["Traumatismos","Cáncer"]])

print ("-"*130)

#Punto 7
print ("Punto 7")
print ("A continuación se muestran los  datos de pacientes con enfermedad general que superen los 40000")
print ("-"*30)
patientsList2= [32121,14564,65465,85202,93213,100231]
mayores= lambda elemento: elemento > 40000
ListaMayores= list (filter(mayores, patientsList2))
print (ListaMayores)

#Punto 8
print ("Punto 8")
print ("A continuación se muestra en pantalla la multiplicación por 10% de los pacientes de cáncer")
print ("-"*30)

List= [6541,4334,4323,34545,5454,7675]
multiplicar= lambda numero : numero*0.1
listaMultiplicar= list(map(multiplicar, List))
print (listaMultiplicar)

#Punto 9
print ("Punto 9")
print ("A continuación se muestra en pantalla la suma de pacientes por traumatismo")
print ("-"*30)

from functools import reduce
list2= [6545,43243,67657,435435,345345,43543]
sumar= lambda acumulado = 0, elemento = 0: acumulado + elemento 
suma= reduce (sumar, list2)
print (suma)

print ("-"*130)