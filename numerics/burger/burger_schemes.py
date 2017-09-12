import numpy as np
import matplotlib.pyplot as plt

import initial as ic


def FTBS_burger(phiOld, dt, dx):

	nx = len(phiOld)

	phi= np.zeros_like(phiOld)	

	for j in xrange(1, nx):
		phi[j] = phiOld[j] - phiOld[j] * (dt/dx) * (phiOld[j] - phiOld[j-1])
	# Apply periodic boundary conditions
	phi[0] = phi[-1]

	return phi


def FTCS_burger(phiOld, dt, dx):

	nx = len(phiOld) - 1

	phi= np.zeros_like(phiOld)

	for j in xrange(1, nx):
		phi[j] = phiOld[j] - phiOld[j] * (dt/(2*dx)) * (phiOld[j+1]-phiOld[j-1])
	# Apply periodic boundary conditions
	phi[0] = phiOld[0] + phiOld[0] * (dt/(2*dx)) * (phiOld[1]-phiOld[-2])
	phi[nx] = phi[0]

	return phi


def CTCS_burger(phi, phiOld, dt, dx):

	nx = len(phiOld) - 1

	phiNew= np.zeros_like(phiOld)

	for j in xrange(1, nx):
		phiNew[j] = phiOld[j] - phi[j]*(dt/dx)*(phi[j+1]-phi[j-1])
	# Apply periodic boundary conditions
	phiNew[0] = phiOld[0] + phi[0]*(dt/dx)*(phi[1]-phi[-2])
	phiNew[nx] = phiNew[0]

	return phiNew


def FTCS_burger_c(phiOld, c, dx):

	nx = len(phiOld) - 1

	phi= np.zeros_like(phiOld)

	dt = c * dx / np.max(phiOld)
	print("Time Step: "+str(dt))

	for j in xrange(1, nx):
		phi[j] = phiOld[j] - phiOld[j] * (dt/(2*dx)) * (phiOld[j+1]-phiOld[j-1])
	# Apply periodic boundary conditions
	phi[0] = phiOld[0] + phiOld[0] * (dt/(2*dx)) * (phiOld[1]-phiOld[-2])
	phi[nx] = phi[0]

	return phi, dt


def CTCS_burger_c(phi, phiOld, c, dx):

	nx = len(phiOld) - 1

	phi= np.zeros_like(phiOld)

	dt = c * dx / np.max(phiOld)
	print("Time Step: "+str(dt))

	for j in xrange(1, nx):
		phiNew[j] = phiOld[j] - phi[j]*(dt/dx)*(phi[j+1]-phi[j-1])
	# Apply periodic boundary conditions
	phiNew[0] = phiOld[0] + phi[0]*(dt/dx)*(phi[1]-phi[-2])
	phiNew[nx] = phiNew[0]

	return phiNew, dt


if __name__ == "__main__":

	nx = 5
	x = np.linspace(0., 1, nx)
	dx = 1./nx
	dt = 1

	nt = 1
	u = np.zeros(nx)
	u[1] = 2.
	u[2] = 1.
	
	#print(phi)

	u_new = FTBS_burger(u, dt, dx)

	print(x)
	print(u)
	print(u_new)



