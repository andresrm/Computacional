 
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


#    Dados 10 puntos aleatorios entre x=0 y x=3 para la función f(x) = sin(2 x).
x0 = 3*np.random.random(10)
y0 = np.sin(2*x0)
#    Dados 20 puntos aleatorios entre x=-10 y x=10 para la función f(x) = sin(x)/x
x1 = 20*np.random.random(20) -10
y1 = np.sin(x1)/x1
#    Dados 16 puntos aleatorios entre x=-3 y x=3 para la función f(x) = x^2 sin(2 x)
x2 = 6*np.random.random(16) - 3
y2 = x2*x2 *np.sin(2*x2)
#    Dados 12 puntos aleatorios entre x=-2 y x=2 para la función f(x) = x^3 sin(3 x)
x3 = 4*np.random.random(12) -2
y3 =  x3*x3*x3*np.sin(3*x3)



# Array with points in between those of the data set for interpolation.
x_0 = np.linspace(min(x0),max(x0),100)
x_1 = np.linspace(min(x1),max(x1),100)
x_2 = np.linspace(min(x2),max(x2),100)
x_3 = np.linspace(min(x3),max(x3),100)

# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')



#plot 1
plt.plot(x0, y0, 'o', label='Data')
for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x_0, f(x_0), label=o)      # plot of interpolated data
plt.title('f(x) = sin(2 x)')
plt.legend()
plt.show()

#plot2
plt.plot(x1, y1, 'o', label='Data1')
for o in options:
    f = interp1d(x1, y1, kind=o)    # interpolation function
    plt.plot(x_1, f(x_1), label=o)      # plot of interpolated data
plt.title('f(x) = sin(x)/x')
plt.legend()
plt.show()

#plot3
plt.plot(x2, y2, 'o', label='Data2')
for o in options:
    f = interp1d(x2, y2, kind=o)    # interpolation function
    plt.plot(x_2, f(x_2), label=o)      # plot of interpolated data
plt.title('f(x) = x^2 sin(2 x)')
plt.legend()
plt.show()

#plot4
plt.plot(x3, y3, 'o', label='Data3')
for o in options:
    f = interp1d(x3, y3, kind=o)    # interpolation function
    plt.plot(x_3, f(x_3), label=o)      # plot of interpolated data
plt.title('f(x) = x^3 sin(3 x)')
plt.legend()
plt.show()

