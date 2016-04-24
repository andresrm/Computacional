
from math import sin,cos,pi

r = float(input("Introduce r: "))

d = float(input("Ingresa theta en grados: "))

theta = d*pi/180

x = r*cos(theta)

y = r*sin(theta)

print("x =",x," y =",y)