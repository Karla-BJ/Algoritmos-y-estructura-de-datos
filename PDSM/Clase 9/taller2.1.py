import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import math 
df = pd.read_csv('Clase 9/resp.csv')
resp = df['resp']

fs = 125
N = len(resp)
Tt = N/fs #Tiempo total que es como el periodo total 
f1 = 1/Tt #Frecuencia natural 
t = (np.arange(0,len(resp))-1)/fs #Para tener los valores correspondientes

f = np.zeros(round(N/2))
X_mag = np.zeros(round(N/2)) 
X_phase = np.zeros(round(N/2)) 

for m in range(1,round(N/2)):
    f[m] = m*f1 #Se define el vector para graficar después, m es la variable de interación 
    a = np.sum(resp*(np.cos(2*np.pi*f[m]*t))) #Se calcula con la ecuación de clase
    b = np.sum(resp*(np.sin(2*np.pi*f[m]*t)))
    X_mag[m] = np.sqrt((a*2) + (b*2)) #Magnitud del espectro (C mayúscula en las diap. --> pitágoras)
    X_phase[m] = -math.atan2(b,a) #Tangente inversa de b/a (Desfase) 


# Convert Phase to degrees
X_phase = np.unwrap(X_phase) #Sacar múltiplos de 360 
X_phase = (X_phase*360)/(2*np.pi)#Radianes a grados 
#Pasar de radianes a grados 
ax = plt.subplot(2,1,1)
plt.plot(f,X_mag)              
plt.xlabel('Frequency (Hz)',fontsize= 14)
plt.ylabel('|X(m)|',fontsize= 14)
ax = plt.subplot(2,1,2)
plt.plot(f,X_phase)              
plt.xlabel('Frequency (Hz)',fontsize= 14)
plt.ylabel('Phase (deg)',fontsize= 14)
plt.figure()
plt.plot(resp)
plt.show()

# FFT: Modulo FFT funcion fft 
X = np.fft.fft(resp) #fft.fft es para determinar la liberia --> Se resuelve por números complejos que están duplicados en dos espectros, real e imaginario, la frecuencia más comun en la señal
X_mag = np.abs(X) #es para obtener la parte real 

f = (fs)*(np.arange(1,N+1)/N)
#plt.plot(f,X_mag)
#plt.show()

N2 = np.round(N/2)
f2 = (fs/2)*(np.arange(1,N2+1)/N2)
X_mag2 = X_mag[0:int(N2)] #La mitad de z-mag va desde 0 hasta la mitad de xmag 
plt.figure()
plt.plot(f2,X_mag2)
plt.show()