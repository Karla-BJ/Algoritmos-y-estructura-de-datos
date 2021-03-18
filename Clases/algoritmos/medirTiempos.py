import time
tiempoInicial = time.time()
print ("hola a todos")
tiempoFinal = time.time()
delta= tiempoFinal-tiempoInicial
print (delta)
#----Inicio conteo----#
timeInicial = time.time()
#----Instrucciones----#
print("hola a todos")
for i in range (1000):
    print(i)
#----Cierre de conteo----#
tiempoFinal = time.time()
delta = tiempoFinal-timeInicial
print(delta)


#----Inicio conteo----#
time2Inicial = time.time()
#----Instrucciones----#
print("hola a todos")
x = 123
for j in range (x):
    print(j)
#----Cierre de conteo----#
tiempoFinal = time.time()
delta = tiempoFinal-time2Inicial
print(delta)