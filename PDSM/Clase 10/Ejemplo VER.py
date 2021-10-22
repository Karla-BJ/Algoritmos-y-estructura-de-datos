import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('ver.csv', header=None)
cols = df.columns
ver = df[cols[:]]
ver = ver.values

plt.subplot(2,1,1)
plt.plot(ver[:,5]) #Todas las filas de la columna 27
plt.title('Un solo potencial evocado')

ver_avg = np.mean(ver, axis=1) #Promediar todas punto a punto para obtener una señal (Axis son filas)
plt.subplot(2,1,2)
plt.plot(ver_avg)
plt.title('El promedio de 100 potenciales evocados')
plt.show()
#Esto sirve para señales períodicas que mantienen en una sola posición porque así puedo compararlas sin que se afecte la onda original 