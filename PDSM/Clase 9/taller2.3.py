import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import math 

#Punto A
df = pd.read_csv('Clase 9/ecg_sine_noise.csv')
ecg = df['ECG']
fs = 1000
N = len(ecg)
X = np.fft.fft(ecg) 
X_mag= np.abs(X)

N2 = np.round(N/2) 
f = (fs/2)*(np.arange(1,N2+1)/N2) 
X_mag2 = X_mag[0:int(N2)]
plt.figure()
plt.plot(f,X_mag2)
plt.show()

'''#Punto B --> Profe, no sé que hice jajajaja
aux= np.where (f>60)
ind= aux[0][0]
print (ind)
aux_index= np.arange(0,int(ind))
X[aux_index]= 0 + 0j

# Reconstruction (ifft) #Transformada de furier inversa
aux_index = np.arange(0,301) #Del 0 al 4 no se apaga --> del 496 al 500 tampoco porque son espejo
X[aux_index] = 0 + 0j #j es por imaginario, se apagan poniendolos en 0, ¿Cuáles de X debo apagar?
aux_index = np.arange(N-301-1,N)
X[aux_index] = 0 + 0j
sig_r = np.fft.ifft(X)
sig_r = np.real(sig_r)

plt.figure()
plt.plot(sig_r)
plt.plot(ecg, linestyle='dashed')
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('x(t)',fontsize=14)
plt.title('reconstrucción',fontsize=14)
plt.show()'''