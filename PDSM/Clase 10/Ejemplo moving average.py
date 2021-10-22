import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('Clase 10/ecg_noisy.csv')
ecg1 = df['ECG1000']
ecg1 = ecg1 - np.mean(ecg1) #Se resta la media a la señal (Es bueno siempre restarle el promedio a la misma señal)
N = len(ecg1) #4000 posiciones
fs = 1000

plt.subplot(2,2,1)
plt.plot(ecg1)
window = int (fs/40) #Cantidad de puntos de la ventana
ecg_avg = np.zeros(N) #Crear variable llamada N con 4000 elementos de 0 c/u
for i in range(N-window): #Ciclo desde n-window Del 0 al 3984
    ecg_avg[i+window] = np.mean(ecg1[i:i+window]) #Posición que no toca los primeros valores que se decidió que quedara vacío lo primero 

plt.subplot(2,2,3)
plt.plot(ecg_avg)

plt.subplot(2,2,2)
X = np.fft.fft(ecg1) #Espectro
X = np.abs(X)
f = (fs)*(np.arange(1,N+1)/N)
plt.plot(f,X)
plt.xlim((0, fs/2))

plt.subplot(2,2,4)
X = np.fft.fft(ecg_avg)
X = np.abs(X)
f = (fs)*(np.arange(1,N+1)/N)
plt.plot(f,X)
plt.xlim((0, fs/2))
plt.show()
#Hace promedio cada cierta cantidad de puntos, a menor cantidad de puntos, la nueva señal va a ser igual a la original 
#Siempre no voy a tener window-1 cantidad de valores porque queda un espacio 
#Espectro x es frecuencia en hz abajo están atenuados (se atenuaron los componentes de alta frecuencia del espectro --> izquierda), también hay una modificación de 10 y de ahí se atenúa todo conservando las bajas frecuencias 