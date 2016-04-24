
import math

G=6.67e-11
M=5.97e24
R=6371000
pi=3.1416

t= float(input("Periodo del satélite:"))
T= t*60
h=( (G*M*T*T) / (4*pi*pi) )**(1/3) - R

print ("Altura del satélite:", h, "metros.")
