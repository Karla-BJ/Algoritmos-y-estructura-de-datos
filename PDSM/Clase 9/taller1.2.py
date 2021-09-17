import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#Punto 2
df= pd.read_csv('Clase 9/temp.csv')
patron= df["Temp"]
df= pd.read_csv('Clase 9/ppgs.csv')
ppg1= df["PPG1"]
ppg2= df["PPG2"]

npts = 4589
lags = np.arange(-npts +1, npts) #Ver la gráfica desde el -4589 hasta 4589
corr = np.correlate(patron-patron.mean(),ppg1-ppg1.mean(),mode ='full') 

# la normalizamos con pearson
corrP = corr / (npts * ppg1.std() * patron.std())
corrP_Max1= (max(corrP))
print (f"La correlación máxima de pearson en PPG1 es correspondiente a {corrP_Max1}" )

# escriba un código que encuentre la posición del máximo en la correlación
pos = np.argmax (corrP)
maxlag = lags [pos]
print (f"La correlación máxima en PPG1 es correspondiente a {maxlag}" )

plt.plot(patron[:], label='Patron')
plt.plot(ppg1[:], label='PPG1')
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.show()

# Realizamos la correlación cruzada de señal patron sobre ppg2
lags = np.arange(-npts + 1, npts) 
corr = np.correlate(patron - patron.mean(), ppg2 - ppg2.mean(), mode='full')
# la normalizamos con pearson
corrP = corr / (npts * patron.std() * ppg2.std())
corrP_Max2= max(corrP)
print (f"La correlación máxima de pearson en PPG2 es correspondiente a {corrP_Max2}" )

# escriba un código que encuentre la posición del máximo en la correlación
pos = np.argmax (corrP)
maxlag = lags [pos]
print (f"La correlación máxima en PPG2 es correspondiente a {maxlag}" )

x =  np.arange(490,490 + len(patron))
plt.figure()
plt.plot(ppg2, 'b', label='ppg2')
plt.plot(x, patron, 'r', label='patron')
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.show()

if corrP_Max1<=corrP_Max2:
    print('el mayor numero entre', corrP_Max1, 'y', corrP_Max2, 'es ', corrP_Max2, "concluyendo así que la señal PPG2 es la que más se parece al patrón inicial")
else:
    print('el mayor numero entre', corrP_Max1, 'y', corrP_Max2, 'es ', corrP_Max1, "concluyendo así que la señal PPG1 es la que más se parece al patrón inicial")


