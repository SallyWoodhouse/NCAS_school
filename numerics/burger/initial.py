import numpy as np
import matplotlib.pyplot as plt

def initialBell(x):
	return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)


def initialSquare(x):
	return np.where(x%1. < 0.5, 1., 0)
