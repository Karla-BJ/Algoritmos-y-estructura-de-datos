import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# creamos una señal seno y otra coseno y le sumamos "ruido" aleatorio
npts = 500
x = np.linspace(0, 50, npts)
y1 = 5 * np.sin(x/2) + np.random.randn(npts)
y2 = 5 * np.cos(x/2) + np.random.randn(npts)

# realizamos la correlación cruzada
lags = np.arange(-npts + 1, npts) # ¿qué es esto? --> Número de muestras (npts) para definir el tamaño de X
corr = np.correlate(y1 - y1.mean(), y2 - y2.mean(), mode='full') #--> para darle los valores en x
# la normalizamos con pearson
corrP = corr / (npts * y1.std() * y2.std())

# graficamos
fig, axs = plt.subplots(nrows=2) #--> nrows: numero de filas
fig.subplots_adjust(hspace=0.4) #--> Espacio entre las gráficas
ax = axs[0]
ax.plot(x, y1, 'b', label='y1')
ax.plot(x, y2, 'r', label='y2')
ax.set_ylim(-10, 10)
ax.legend(loc='upper right', fontsize='small', ncol=2)

ax = axs[1]
ax.plot(lags, corrP)
ax.set_ylim(-1.1, 1.1)
ax.set_ylabel('cross-correlation')
ax.set_xlabel('lag of y1 relative to y2')

plt.show()

# comprobación del resultado gráfico
# lag = #?
# plt.plot(y1[lag:], 'b', label='y1')
# plt.plot(y2[:-lag], 'r', label='y2')
# plt.ylim(-10, 10)
# plt.legend(loc='upper right', fontsize='small', ncol=2)
# plt.show()

# escriba un código que encuentre la posición del máximo en la correlación

