from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt
import scipy 
import numpy as np

# Configuracion del Diagrama de Ojo
# Ndat: Es el numero de datos a graficar
# Sps: El numero de muestras por simbolo del archivo generado en gnuradio
Ndat=100000 
Sps = 8

# Leemos el archivo producido por gnuradio
#y0=scipy.fromfile(open("senal0"), dtype=scipy.float32) 
y1=scipy.fromfile(open("senal1"), dtype=scipy.float32) 
y2=scipy.fromfile(open("senal2"), dtype=scipy.float32) 
y3=scipy.fromfile(open("senal3"), dtype=scipy.float32) 
y4=scipy.fromfile(open("senal4"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
#y0=(y0[0:Ndat])
y1=(y1[0:Ndat])
y2=(y2[0:Ndat])
y3=(y3[0:Ndat])
y4=(y4[0:Ndat])



#Grafica1
eyediagram(y1, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("F.Nyquist")
plt.show()

#Grafica2
eyediagram(y2, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("F.RC, rollof=1.0")
plt.show()

#Grafica3
eyediagram(y3, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("F.RC, rollof=0.5")
plt.show()

#Grafica4
eyediagram(y4, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("F.RC, rollof=0-35")
plt.show()

