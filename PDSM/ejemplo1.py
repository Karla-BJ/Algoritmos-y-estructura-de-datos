# Crear una señal senoidal

#Dummy sine plot
import math 
import numpy as np
import matplotlib.pyplot as plt

#a = [0, np.pi/4, np.pi/2, np.pi*(3/4), np.pi, np.pi*(5/4), np.pi(3/2)]
a= np.linspace(0,np.pi*2, 100)
plt.plot (np.sin(a))
plt.show()



