# File neural_data.csv contains two waveforms, x and y, that were recorded from two different
# neurons in the brain with a sampling interval of 0.2 ms. They are believed to be involved in the
# same function, but separated by one or more neuronal junctions that impart a delay to the signal.
# Plot the original data, determine if they are related and, if so, the time delay between them.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

neural= pd.read_csv ("neural_data.CSV", encoding= "UTF-8", header=0, delimiter= ";").to_dict()

df = pd.read_csv('neural_data.csv')
n1 = df['Neuron 1']
n2 = df['Neuron 2']
ax1 = plt.subplot(211)
plt.plot(n1)
plt.plot(n2)
plt.title('Neurons 1 and 2')
plt.grid()
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

t= np.linspace(0,stop, fs*stop)
y= np.sin(2*np.pi*f*t)
plt.plot(t,y)
plt.show()

