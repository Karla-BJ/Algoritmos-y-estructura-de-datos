import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('data_example1.csv')
print(df.head(5))
df.plot(x= 'Time', y=['S1','S4'], kind = 'line')
df.plot(x= 'S1', y='S4', kind = 'scatter')

x = df['S1']
y = df['S4']

# Calcule la correlación entre x y y

# Calcule la correlación de pearson entre x y y


