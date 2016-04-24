import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


n=1000

# Arreglos 
x=[]
TT0=[]
x_0=np.linspace(0.001,np.pi + 0.001, n)



#   el integrando
I = lambda x,a: 1/np.sqrt(np.cos(x) - np.cos(a))


for i in range(n):
#   la integral
    theta_0=x_0[i]
    T , err= integrate.quad(I, 0, theta_0, args=(theta_0,))
    
    
#   el error
    TT0.append(np.sqrt(2)/np.pi * T)
    
    
    
#   Gráfica desviación
plt.figure(1)
plt.plot(x_0 * 180 / np.pi, TT0 , "r" )
plt.title('Desviación periodo real - aproximación')
plt.xlabel(r'$ \theta _0 (deg)$')
plt.ylabel("T/To")
plt.xlim(0,90)
plt.ylim(1,1.2)
plt.grid()


plt.show()


#   Gráfica divergencia
plt.figure(1)
plt.plot(x_0 * 180 / np.pi, TT0 , "b" )
plt.title('Divergencia en ' r'$\theta_0 = \pi$')
plt.xlabel(r'$ \theta _0 (deg)$')
plt.ylabel("T/To")
plt.xlim(0,180)
plt.ylim(1,5)
plt.grid()


plt.show()