import numpy as np
import matplotlib.pyplot as plt

import initial as ic
import burger_schemes as scheme


def run_FTBS(U, dx, dt, nt):

	UOld = U.copy()
	c_calculated = np.zeros(nt)

	for n in xrange(0, nt):
		U = scheme.FTBS_burger(UOld, dt, dx)

		c_calculated[n] = np.max(U*dt/dx)

		#update for next time step
		UOld = U.copy()

	return U, c_calculated


def run_FTCS(U, dx, dt, nt):

	UOld = U.copy()
	c_calculated = np.zeros(nt)

	for n in xrange(0, nt):
		U = scheme.FTCS_burger(UOld, dt, dx)

		c_calculated[n] = np.max(U*dt/dx)

		#update for next time step
		UOld = U.copy()

	return U, c_calculated


def run_CTCS(U, dx, dt, nt):

	UOld = U.copy()
	UNew = U.copy()

	c_calculated = np.zeros(nt)

	U = scheme.FTBS_burger(UOld, dt, dx)
	c_calculated[0] = np.max(U*dt/dx)

	for n in xrange(1, nt):
		UNew = scheme.CTCS_burger(U, UOld, dt, dx)

		c_calculated[n] = np.max(UNew*dt/dx)

		#update for next time step
		UOld = U.copy()
		U = UNew.copy()

	return U, c_calculated


nx = 40
x = np.linspace(0., 1, nx+1)
#c = 0.5
dx = 1./nx
dt = 0.001

nt = 200
time_step = np.arange(1, nt+1)
dt_generated = np.zeros(nt)
c_calculated = np.zeros(nt)

u = ic.initialBell(x)
#u = ic.initialSquare(x)
#uNew = u.copy()
#uOld = u.copy()

u_FTBS, c_FTBS = run_FTBS(u, dx, dt, nt)
u_FTCS, c_FTCS = run_FTCS(u, dx, dt, nt)
u_CTCS, c_CTCS = run_CTCS(u, dx, dt, nt)


# Plotting
plt.figure(1)
#plt.plot(x, ic.initialBell(x), 'k', label = 'initial')
plt.plot(x, u_FTBS, 'r', label = 'FTBS')
plt.plot(x, u_FTCS, 'b', label = 'FTCS')
plt.plot(x, u_CTCS, 'k', label = 'CTCS')
plt.legend(loc='best')
plt.title(str(nt*dt)+" time")

plt.figure(2)
plt.plot(time_step, c_FTBS, 'r', label = 'FTBS')
plt.plot(time_step, c_FTCS, 'b', label = 'FTCS')
plt.plot(time_step, c_CTCS, 'k', label = 'CTCS')
plt.legend(loc='best')
plt.ylabel("Courant number")
plt.title(str(nt*dt)+" time")

plt.show()

