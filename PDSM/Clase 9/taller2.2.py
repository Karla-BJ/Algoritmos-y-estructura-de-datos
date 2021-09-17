from numpy.core.fromnumeric import argmax
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import math 
df = pd.read_csv('Clase 9/ecg_1min.csv')
ecg = df['ECG']
fs = 250
N = len(ecg)
# FFT
X = np.fft.fft(ecg)
X_mag = np.abs(X)

# Frequency vector completo
#f = (fs)*(np.arange(1,N+1)/N)
#plt.plot(f,X_mag)
#plt.show()

# Frequency vector (half!)
N2 = np.round(N/2)
f2 = (fs/2)*(np.arange(1,N2+1)/N2)
X_mag2 = X_mag[0:int(N2)]
plt.figure()
plt.plot(f2,X_mag2)
plt.xlim(0,20) #Zoom en la función ej en una frecuencia determinada 
plt.show()

#punto B
N2 = np.round(N/2)
f2 = (fs/2)*(np.arange(1,N2+1)/N2) #Corte en la frecuencia
X_mag2 = X_mag[0:int(N2)]
plt.figure()
plt.plot(f2,X_mag2)
plt.xlim(0.66,3) #--> regla de 3 para cortarlo
plt.show()
# Lo que haremos con este ciclo for es decir los parametros dados en el laboratorio de 40 a 180 latidos por minuto 
fz = []
xz = []
plt.figure()
for posicion in range(len(f2)):
    if f2[posicion]>0.66 and f2[posicion]<=3: 
        fz.append(f2[posicion])
        xz.append(X_mag2[posicion])

# Calculamos la fecuencia cardiaca
plt.grid() #CUadrícula
plt.plot(fz,xz)

mfrec = fz[xz.index(max(xz))] #Valor máximo de la gráfica y lo multilica por 60 para convertirlo en lpm
mfrec = mfrec*60
print("El número de latidos promedio es de ", mfrec, "latidos por minuto")