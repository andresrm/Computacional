
from math import sin,cos,pi

r = float(input("Introduce r: "))

d = float(input("Ingresa theta en grados: "))

f = float(input("Ingresa phi en grados: "))

theta = d*pi/180
phi = f*pi/180 


x = r*sin(theta)*cos(phi)

y = r*sin(theta)*sin(phi)

z = r*cos(theta)

print("x =",x," y =",y, " z = ",z)