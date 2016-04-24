import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt



data = np.loadtxt('data.txt')

x=data[:,0].astype(np.int)
y=data[:,1].astype(np.float)


xn=np.linspace(1900,2000,2)

m, c = np.polyfit(x, y, 1)
yn = np.polyval([m, c], xn)

plt.plot(x, y, 'or', label="Datos")
plt.plot(xn, yn, label="Ajuste")
plt.title('Ajuste lineal, temperatura New York')
plt.legend()
plt.show()


data1=np.loadtxt('data1.txt')

x1=data1[:,0].astype(np.int)
y1=data1[:,1].astype(np.float)


def f(x,u,v,w):
    return u*np.exp(-v*x) + w
    
    
popt, pcov = optimize.curve_fit(f, x1, y1)


    
xm=np.linspace(-0,50,1000)

plt.plot(x1, y1, 'or', label="Datos")
plt.plot(xm,f(xm,*popt), label="Ajuste")

plt.title('Ajuste exponencial, presión-altitud')
plt.legend()
plt.show()
