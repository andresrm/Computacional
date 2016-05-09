# zombie apocalypse modeling
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8


P = 0       # birth rate
d = 0.0000  # natural death percent (per day)
B = 0.0095  # transmission percent  (per day)
G = 0.0001  # resurect percent (per day)
A = 0.0001  # destroy percent  (per day)
r = 0.5000  # infection rate 
k = 0.0220  # infected on quarentine rate
s = 0.0220  # zombies on quarentine rate
e = 0.0010  # killed because escaping
c = 0.200  # cure effectiveness rate


# Los modelos 
def Basic(y, t):
	Si = y[0]
	Ii = y[1]
	Zi = y[2]
	Ri = y[3]	
	f0 = P - B*Si*Zi - d*Si
	f1 = B*Si*Zi + G*Ri - A*Si*Zi
	f2 = d*Si + A*Si*Zi - G*Ri
	return [f0, f2, f1, 0, 0]

def LatentInfection(y, t):
	Si = y[0]
	Ii = y[1]
	Zi = y[2]
	Ri = y[3]
	f0 = P - B*Si*Zi - d*Si
	f1 = B*Si*Zi - r*Ii - d*Ii
	f2 = r*Ii + G*Ri - A*Si*Zi
	f3 = d*Si + d*Ii + A*Si*Zi - G*Ri
	return [f0, f1, f2, f3, 0]


def Quarantine(y,t):
	Si = y[0]
	Ii = y[1]
	Zi = y[2]
	Ri = y[3]
	Qi = y[4]	
	f0 = P - B*Si*Zi - d*Si
	f1 = B*Si*Zi - r*Ii - d*Ii - k*Ii
	f2 = r*Ii + G*Ri - A*Si*Zi - s*Zi
	f3 = d*Si + d*Ii + A*Si*Zi - G*Ri + e*Qi
	f4 = k*Ii + s*Zi - e*Qi	
	return [f0, f1, f2, f3, f4]
	
def Treatment(y,t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
    f0 = P - B*Si*Zi - d*Si + c*Zi
    f1 = B*Si*Zi - r*Ii - d*Ii
    f2 = r*Ii + G*Ri - A*Si*Zi - c*Zi
    f3 = d*Si + d*Ii + A*Si*Zi - G*Ri
    return [f0, f1, f2, f3, 0]



# initial conditions
S0 = 500.                   # initial population
I0 = 0                      # initial infected people
Z0 = 0                      # initial zombie population
R0 = 0                      # initial death population
Q0 = 0                      # initial quarantine population

y0 = [S0, I0, Z0, R0, Q0]   # initial condition vector

t  = np.linspace(0, 20., 1000)       # time grid

# solve the DEs and plot
soln = odeint(Basic, y0, t)
S = soln[:, 0]
R = soln[:, 1]
Z = soln[:, 2]
I = soln[:, 3]
Q = soln[:, 4]
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.ylim(-1,501)
plt.title('Zombie Apocalypse - Basic Model Zero Zombies')
plt.show()

# we change the parameters and initial zombies
Z0 = 2
A  = 0.005
y0 = [S0, I0, Z0, R0, Q0]

soln = odeint(Basic, y0, t)
S = soln[:, 0]
R = soln[:, 1]
Z = soln[:, 2]
I = soln[:, 3]
Q = soln[:, 4]
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - Basic Model')
plt.show()

soln = odeint(LatentInfection, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]
Q = soln[:, 4]
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - Latent Infection')
plt.show()

soln = odeint(Quarantine, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]
Q = soln[:, 4]
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - Quarantine')
plt.show()

soln = odeint(Treatment, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]
Q = soln[:, 4]
plt.title('Zombie Apocalypse')
plt.plot(t, S, label='Living')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - Treatment')
plt.show()


# Eradication with impulsive attacks each 2.5 days
A = 0.00545; B = 0.0075; G = 0.09; d = 0.0001
t1  = np.linspace(0, 2.5, 300)
t2  = np.linspace(2.5, 5., 300)
t3  = np.linspace(5, 7.5, 300)
t4  = np.linspace(7.5, 10.,300)

soln = odeint(Basic, y0, t1)
S = soln[:, 0]
Z = soln[:, 2]
sol1 = odeint(Basic,[soln[299, 0],soln[299, 1],0.75*soln[299, 2],0,0], t2)
S = np.concatenate((S,sol1[:, 0]))
Z = np.concatenate((Z,sol1[:, 2]))
sol2 = odeint(Basic,[sol1[299, 0],sol1[299, 1],0.50*sol1[299, 2],0,0], t3)
S = np.concatenate((S,sol2[:, 0]))
Z = np.concatenate((Z,sol2[:, 2]))
sol3 = odeint(Basic,[sol2[299, 0],sol2[299, 1],0.25*sol2[299, 2],0,0], t4)
S = np.concatenate((S,sol3[:, 0]))
Z = np.concatenate((Z,sol3[:, 2]))


t = np.concatenate((t1,t2,t3,t4))

plt.plot(t, Z, color= 'g' , label='Zombies')
plt.xlabel('Days from outbreak')
plt.ylabel('Zombies')
plt.title('Zombie Apocalypse - Eradication')
plt.show()