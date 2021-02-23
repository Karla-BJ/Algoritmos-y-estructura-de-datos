import pandas as pd
listaVariada= ["a",1,2,3,4]
print (listaVariada)
print ("-"*60)

seriesPandas= pd.Series ([1,2,3])
print (seriesPandas)
print ("-"*60)
seriesPandas= pd.Series ([1.2,4.6,4.9])
print (seriesPandas)
print ("-"*60)

#Sin diccionario#
seriesGananciaPorMes= pd.Series ([4300,4545,2324,1244])
print (seriesGananciaPorMes)

#Con diccionario#
dicGanancias= {}
dicGanancias["Enero"]= 4300
dicGanancias["Febrero"]= 4545
dicGanancias["Marzo"]= 2324
dicGanancias["Abril"]= 1244
seriesGananciaPorMes= pd.Series (dicGanancias)
#Para elegir mostrar solo uno#
print (seriesGananciaPorMes["Enero"])
print ("-"*60)

#Para hacer matrices#
matrizEstudiantesDic = {
                        "Grupo 1" : ['Karla', 'Mario', 'Laura'],
                        "Grupo 2" : ['Santi', 'Arturo', 'Vale'],
                        "Grupo 3" : ['Juan', 'Melany', 'Laura'],
                        "Grupo 4" : ['Mafer', 'Esteban', "Daniel"],
                    
}
dataFrameNombres= pd.DataFrame(matrizEstudiantesDic)
print (dataFrameNombres)
print ("-"*60)
dataFrameNombresDic= pd.DataFrame(matrizEstudiantesDic)
print (dataFrameNombresDic)
print ("-"*60)
print (dataFrameNombresDic ["Grupo 1"])
print ("-"*60)
print (dataFrameNombresDic.iloc[1:])
print ("-"*60)

dicVentasPorMes= {
    "Marzo (millones de pesos)" :[1234,4567,4352],
    "Abril (millones de pesos)" :[4738,3287,2372],
    "Mayo (millones de pesos)" :[2456,5422,2457]
}
dataFrameVentas= pd.DataFrame (dicVentasPorMes, index = ["Tomates","Papa", "Yuca"])
print(dataFrameVentas)