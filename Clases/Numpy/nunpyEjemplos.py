import numpy as np
lista= [1,2,3,4]
listaN= np.arange (1,11,1)
print (listaN)
print ("-"*30)
print (listaN[:5])
print ("-"*30)

#para saltar de x en x#
listaNu= np.arange (1,21,1)
print (listaNu)
print ("-"*30)
print (listaNu[::2])
print ("-"*30)
listaNu[::2]=200
print (listaNu)
print ("-"*30)

#indexación lógica#
edades=[14,23,56,73]
edades= np.array (edades)
indEdades= edades > 18
print (edades)
print ("-"*30)
print (indEdades)
print ("-"*30)
totalMayorEdad= np.sum (indEdades)
print (totalMayorEdad)
print ("-"*30)
indEdades2= edades == 23
indEdades3= edades == 56
indEdades4= indEdades2 | indEdades3
print (indEdades2)
print ("-"*30)
print (indEdades3)
print ("-"*30)
print (indEdades4)
print ("-"*30)
print (np.sum(indEdades4))
print ("-"*30)

#entre 23 y 50#

indEdadesIntervalo1= edades >= 23
indEdadesIntervalo2= edades <= 50
indEdadesIntervalo= indEdadesIntervalo2 & indEdadesIntervalo1
print(np.sum (indEdadesIntervalo))
print ("-"*30)

#Promedio
print (np.mean(edades))
print ("-"*30)

#---mamá---#
mamas = [54,67,34,56]
mamas = np.array (mamas)
hijosMayores30= edades > 0
print(hijosMayores30)
mamas= (mamas[hijosMayores30])
print(mamas)
print ("-"*30)
print (np.mean (mamas[hijosMayores30]))
print ("-"*30)

#Crear matriz con numpy
edadesHijos= np.array([14,18,22,24])
edadesMamas= np.array([45,54,67,74])
childrenMoms= np.array ([edadesHijos, edadesMamas])
print (childrenMoms)
print ("-"*30)

#trasponer matriz
indKids= childrenMoms[0] >= 18
print (childrenMoms.transpose())
print ("-"*30)
print (np.sum (indKids))
print ("-"*30)
print (np.mean (childrenMoms [1][indKids]))
