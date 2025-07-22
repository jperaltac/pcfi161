# Escriba un programa que grafique los datos de tiempo vs posición de un lanzamiento de proyectil. 
# Los datos provienen del fichero :
# https://gitarra.cl/lectures/pcfi161/-/raw/main/general/data1.dat
# En el gráfico utilice nombres y unidades para los ejes. Así como también un color adecuado.
# Una vez finalizado, adjunte comprimido su gráfico y su código

import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("data4.dat",float)

x = datos[:,0]
y = datos[:,1]
x_max, x_min =np.max(x),np.min(x)
y_max, y_min =np.max(y),np.min(y)
plt.plot(x,y,color ="red",label ="Proyectil")
plt.ylim(y_min,y_max)
plt.xlim(x_min,x_max)
plt.title("Grafico lanzamiento de proyectil")
plt.ylabel("Posición(m)")
plt.xlabel("Tiempo(s)")
plt.legend()
plt.show()