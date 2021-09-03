# Crear una señal senoidal

#Dummy sine plot
import math 
import numpy as np
import matplotlib.pyplot as plt

#a = [0, np.pi/4, np.pi/2, np.pi*(3/4), np.pi, np.pi*(5/4), np.pi(3/2)]
# a= np.linspace(0,np.pi*2, 100)
# plt.plot (np.sin(a))
# plt.show()

#Elegant sine plot
fs= 1000 #in Hz
stop= 5  #in seconds
f= 2 # in Hz

t= np.linspace(0,stop, fs*stop)
y= np.sin(2*np.pi*f*t)
plt.plot(t,y)
plt.show()

