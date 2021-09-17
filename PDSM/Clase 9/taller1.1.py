# File neural_data.csv contains two waveforms, x and y, that were recorded from two different
# neurons in the brain with a sampling interval of 0.2 ms. They are believed to be involved in the
# same function, but separated by one or more neuronal junctions that impart a delay to the signal.
# Plot the original data, determine if they are related and, if so, the time delay between them.

#Punto 1

import math 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
fs = 1/0.0002
df = pd.read_csv('neural_data.csv')
n1 = df['Neuron 1'].to_numpy ()
n2 = df['Neuron 2'].to_numpy () #-->Para normalizar la gráfica

y= len (n1)
t= (np.arange(0, y)-1) / fs

# A
plt.figure ()
plt.plot (t, n1)
plt.plot (t, n2)
plt.xlabel ("Tiempo (S)")
plt.show ()

# B
desfase= np.arange (-y +1, y)
corr = np.correlate(n1 - n1.mean(), n2 - n2.mean(), mode='full') #--> Se resta la media y compara todos los datos de la gráfica


maxdes= desfase [np.argmax (corr)]
print (f"La correlación máxima entre N1 y N2, está en el desfase correspondiente a {maxdes}" )
plt.show()

plt.figure()
plt.plot(n1[:maxdes],"b", label="N1") #De -65 hacia adelante
plt.plot(n2[-maxdes:],"r", label="N2") #Hasta 65
plt.legend(loc='upper right', fontsize= 'small', ncol=2)
plt.show()

#Punto C
#Evidentemente las señales neuronales están asociadas al mismo proceso, como prueba de ello tenemos las 
#correlaciones realizadas en el código que nos muestran que hay una gran similaridad en los datos.