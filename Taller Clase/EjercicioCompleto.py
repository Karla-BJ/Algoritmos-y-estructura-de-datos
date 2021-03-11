#Crear un elemento donde muestre las ventas mes a mes
#De una empresa durante un año
import pandas as pd
dicEarningsPerYear= {}
dicEarningsPerYear ["Enero"] = 1234124
dicEarningsPerYear ["Febrero"] = 1562148
dicEarningsPerYear ["Marzo"] = 1526974
dicEarningsPerYear ["Abril"] = 1136528
dicEarningsPerYear ["Mayo"] = 1154789
dicEarningsPerYear ["Junio"] = 1736492
dicEarningsPerYear ["Julio"] = 1288456
dicEarningsPerYear ["Agosto"] = 1325894
dicEarningsPerYear ["Septiembre"] = 1115589
dicEarningsPerYear ["Octubre"] = 1125877
dicEarningsPerYear ["Noviembre"] = 1458962
dicEarningsPerYear ["Diciembre"] = 1154899
serieEarningsPerYear= pd. Series (dicEarningsPerYear)
print (serieEarningsPerYear)
print ("-"*30)

#Muestre en pantalla las ganancias por trimestre

dicEarningsThreeMonth= {}
dicEarningsThreeMonth ["1er Trimestre"] = sum (serieEarningsPerYear[ "Enero":"Marzo"])
dicEarningsThreeMonth ["2do Trimestre"] = sum (serieEarningsPerYear[ "Abril":"Junio"])
dicEarningsThreeMonth ["3er Trimestre"] = sum (serieEarningsPerYear[ "Julio":"Septiembre"])
dicEarningsThreeMonth ["4to Trimestre"] = sum (serieEarningsPerYear[ "Octubre":"Diciembre"])
serieEarningsThreeMonth= pd. Series(dicEarningsThreeMonth)
print (serieEarningsThreeMonth)
print ("la suma total del año es igual a: ")
print ( sum(serieEarningsPerYear))
print ("-"*30)

#Ganancias mensuales por departamento: Antioquia, Amazonas, Cundinamarca

dicEarningsXDpto= {
    "Antioquia": [26164961,6149626,5614626,66216326,16144926,2694826659],
    "Amazonas": [15484694,16648466,1516216,66948269,6156564,2614462],
    "Cundinamarca": [5154694,16194943,6494666,4959562,65949595,5595956]
} 
listaMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
dataFrameEarningsXDpto = pd.DataFrame(dicEarningsXDpto, index= listaMeses)
print (dataFrameEarningsXDpto)

print (dataFrameEarningsXDpto["Marzo":"Mayo"][["Antioquia","Amazonas"]])