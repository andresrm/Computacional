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
Err=[]
x_0=np.linspace(0.001,np.pi + 0.001, t)

#   el integrando
I = lambda x,a: 1/np.sqrt(np.cos(x) - np.cos(a))

for i in range(t):
#   la integral
    theta_0=x_0[i]
    T_0 , err= integrate.quad(I, 0, theta_0, args=(theta_0,))
    
    
#   el error
    TT0_0.append((4/np.sqrt(2)) * T_0)



    

for i in range(t):
    
    
        theta_0 = x_0[i]
        T0=1
        
        for u in range(10):
            sen=0
            for k in range(50):
                sen += math.pow(-1,k)/math.factorial(2*k+1) * math.pow(theta_0/2, 2*k+1)
            
            T0 += math.pow( math.factorial(2*(u+1)) / (math.pow( math.pow(2,(u+1)) * math.factorial(u+1) , 2 ) ) , 2 ) * math.pow( sen , 2*(u+1) )   
            
           
        Err.append(100*(np.absolute(2 * np.pi * T0 - TT0_0[i])/TT0_0[i]))
   
    

plt.plot(x_0 * 180 / np.pi, Err, '-.', linewidth=2, label='$T %i $' % (2*v))
    
    

   
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