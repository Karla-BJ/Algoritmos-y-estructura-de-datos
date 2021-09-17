#Análogo del ejemplo 2
import numpy as np
import matplotlib.pyplot as plt 
import math 
#Para hacer recontrucción con ifft, no puedo sacarle el valor absoluto --> Porque estaría eliminando la parte imaginaria (Todo estaría mal)

fs = 500          
Tt = 1            
N = Tt*fs          
f1 = 1/Tt     
t = np.arange(1,N+1)/fs 

# Construct waveform 
sig = np.zeros(N)
sig[0:int(N/2)] = t[0:int(N/2)]
plt.plot(t,sig)

# FFT
X = np.fft.fft(sig)
#X = np.abs(X)

# Reconstruction (ifft) #Transformada de furier inversa
aux_index = np.arange(5,N-4) #Del 0 al 4 no se apaga --> del 496 al 500 tampoco porque son espejo
X[aux_index] = 0 + 0j #j es por imaginario, se apagan poniendolos en 0, ¿Cuáles de X debo apagar?
sig_r = np.fft.ifft(X)
sig_r = np.real(sig_r)

plt.figure()
plt.plot(t,sig_r)
plt.plot(t,sig, linestyle='dashed')
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('x(t)',fontsize=14)
plt.title('5 components reconstruction',fontsize=14)
plt.show()