import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math

t=100
n=6
# Arreglos 
x=[]
TT0_0=[]
TT0=[]
x_0=np.linspace(0.001,np.pi + 0.001, t)

#   el integrando
I = lambda x,a: 1/np.sqrt(np.cos(x) - np.cos(a))

#   Calcular los valores reales
for i in range(t):
#   la integral
    theta_0=x_0[i]
    T_0 , err= integrate.quad(I, 0, theta_0, args=(theta_0,))
    
    
#   el periodo
    TT0_0.append((4/np.sqrt(2)) * T_0)

    
#   Ciclo para cada gráfica:    
for v in range(n):
    
#   lista de los valores de error    
    err=[]
        
    for i in range(t):
    
    
        theta_0 = x_0[i]
        T0=1

#   la sumatoria        
        for u in range(v):
            
            T0 += math.pow( math.factorial(2*(u+1)) / (math.pow( math.pow(2,(u+1)) * math.factorial(u+1) , 2 ) ) , 2 ) * math.pow( np.sin(theta_0 / 2), 2*(u+1) )   
            
#   los valores en la lista de errores           
        err.append(100*(np.absolute(2 * np.pi * T0 - TT0_0[i])/TT0_0[i]))
   
#   Gráfica, cada aproximación    
    plt.plot(x_0 * 180 / np.pi, err, '-.', linewidth=2, label='$T %i $' % (2*v))
    
    

   
#   Gráfica desviación
plt.title('Errores relativos de las series de potencias')
plt.xlabel(r'$ \theta _0 (deg)$')
plt.ylabel("Error Relativo (%)")
plt.xlim(0,120)
plt.ylim(0,1)
plt.xticks(np.arange(0,130,10))
plt.yticks(np.arange(0,1.1,0.1))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
plt.show()


Err=[]
for i in range(t):
    theta_0 = x_0[i]
    T0=1
    for u in range(80):
        sen=0
# la sumatoria para maclaurin en el seno
        for k in range(80):
            sen += math.pow(-1,k)/math.factorial(2*k+1) * math.pow(theta_0/2, 2*k+1)
            
        T0 += math.pow( math.factorial(2*(u+1)) / (math.pow( math.pow(2,(u+1)) * math.factorial(u+1) , 2 ) ) , 2 ) * math.pow( sen , 2*(u+1) )   
    
    Err.append(100*(np.absolute(2 * np.pi * T0 - TT0_0[i])/TT0_0[i]))

plt.plot(x_0 * 180 / np.pi, Err, '-.',color='k', linewidth=2, label='$T %i $' % (2*v))
plt.title('Error usando serie de Maclaurin')
plt.xlabel(r'$ \theta _0 (deg)$')
plt.ylabel("Error Relativo (%)")
plt.xlim(0,180)
plt.ylim(0,1)
plt.xticks(np.arange(0,190,10))
plt.yticks(np.arange(0,1.1,0.1))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
plt.show()