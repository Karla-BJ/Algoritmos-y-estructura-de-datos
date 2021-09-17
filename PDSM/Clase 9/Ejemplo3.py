#Análogo del ejemplo 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math 

df = pd.read_csv('eeg.csv')
print(df.head(5))
#df.plot( y='Amplitude', kind = 'line')

eeg = df['Amplitude']
fs = 50    #Componentes siempre voy hasta la mitad del total
N = len(eeg) #--> det número de muestras

# FFT
X = np.fft.fft(eeg) #fft.fft es para determinar la liberia --> Se resuelve por números complejos que están duplicados en dos espectros, real e imaginario, la frecuencia más comun en la señal
X_mag= np.abs(X) #Valor absoluto

# Frequency vector
f = (fs)*(np.arange(1,N+1)/N)
plt.plot(f,X_mag)
#plt.show()

# Frequency vector (half!)
N2 = np.round(N/2) # Le quito la mitad por los valores duplicados 
f2 = (fs/2)*(np.arange(1,N2+1)/N2) #Me quedo con la mitad de componentes de Fs
X_mag2 = X_mag[0:int(N2)]
plt.figure()
plt.plot(f2,X_mag2)
plt.show()