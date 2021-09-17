import numpy as np
import matplotlib.pyplot as plt 
import math 

fs = 500          #Frecuencia de muestreo
Tt = 1            #Tiempo total --> 1 segundo
N = Tt*fs         #Tamaño --> Número de valores
f1 = 1/Tt     #Frecuencia natural
t = np.arange(1,N+1)/fs 

# Construcción de señal
sig = np.zeros(N) #Hay ceros para llenar el tamaño y luego reemplazalo con los datos que quiero
sig[0:int(N/2)] = t[0:int(N/2)]  #Tomar la mitad de los valores y entrarlos en sig para ponerles el tiempo --> de 1/500 = 0,02 
plt.plot(t,sig)

# Fourier decomposition
a0 = 2*np.mean(sig)
print(a0)
f = np.zeros(round(N/2)) #Variables de interés
X_mag = np.zeros(round(N/2))
X_phase = np.zeros(round(N/2))    
for m in range(1,250): #Ciclo igual al anterio
    f[m] = m*f1
    a = (2/N)*np.sum(sig*(np.cos(2*np.pi*f[m]*t)))
    b = (2/N)*np.sum(sig*(np.sin(2*np.pi*f[m]*t)))
    X_mag[m] = np.sqrt((a**2) + (b**2))
    X_phase[m] = -math.atan2(b,a)

# Reconstruction
sig_r = np.zeros(N)        
for m in range(1,250):
    sig_r = sig_r + X_mag[m]*np.cos(2*np.pi*f[m]*t + X_phase[m])  #Cada posición asignarle un valor --> contador en cada entrada (Proyección de valores de posición en posición)
sig_r = sig_r + a0/2 #Componente DC 

plt.figure()
plt.plot(t,sig_r)
plt.plot(t,sig, linestyle='dashed')
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('sig(t)',fontsize=14)
plt.title('5 components reconstruction',fontsize=14)
plt.show()