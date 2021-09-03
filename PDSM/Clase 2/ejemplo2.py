import pandas
import matplotlib.pyplot as plt
import math

df = pandas.read_csv('PPG2.csv')
print(df)
print(df.columns)
df.plot( y=df.columns, kind = 'line', subplots=True)
plt.show()

signal = df['Anular filtered']
noise = df['Anular'] - signal

#print(type(noise))

def my_snr(signal, noise):

#RMS signal
    aux_s = (signal**2).sum()
    rms_signal = math.sqrt(aux_s/len(signal))
#RMS noise
    aux_n = (noise**2).sum()
    rms_noise = math.sqrt(aux_n/len(noise))
    
    snr_out = 20 * math.log10(rms_signal/rms_noise)
    return snr_out

snr_out = my_snr(signal, noise)
print("SNR is " , snr_out)
#print(len(signal))

#plt.plot(rms_signal)
#plt.show()
#aux_s = sum(signal.^2);
#rms_signal = sqrt(aux_s/length(signal));
#aux_n = sum(noise.^2);
#rms_noise = sqrt(aux_n/length(noise));
#snr_out = 20 * log10(rms_signal./rms_noise);