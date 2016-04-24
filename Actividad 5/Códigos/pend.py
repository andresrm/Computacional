from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -(b/c)*np.sin(theta)]
    return dydt

g = 9.81


l1=5
l2=10

y0 = [np.pi - 0.1, 0.0]

t = np.linspace(0, 50, 101)


sol1 = odeint(pend, y0, t, args=(g,l1))

plt.subplot(211)
plt.plot(t, sol1[:, 0], 'b', label='theta(t)')
plt.grid()
plt.ylabel('theta')

plt.title('Longitud de péndulo l = 5 m')

plt.subplot(212)
plt.plot(t, sol1[:, 1], 'g', label='omega(t)')
plt.grid()
plt.ylabel('omega')
plt.xlabel('t')


plt.show()

sol2 = odeint(pend, y0, t, args=(g,l2))

plt.subplot(211)
plt.plot(t, sol2[:, 0], 'b', label='theta(t)')
plt.grid()
plt.ylabel('theta')

plt.title('Longitud de péndulo l = 10 m')

plt.subplot(212)
plt.plot(t, sol2[:, 1], 'g', label='omega(t)')
plt.grid()
plt.ylabel('omega')
plt.xlabel('t')


plt.show()