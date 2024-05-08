#!/usr/bin/python
#%matplotlib inline
#
# Import needed libraries
#
import os
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 10})
import numpy as np
#
# Read in output of ddPSI
#
data=np.genfromtxt('log_anneal.lammps', usecols=[0,1,2,3,4,5,6], skip_header=4, skip_footer=41)
time=[x[1] for x in data]
temperature=[x[2] for x in data]
energy=[(x[3]/500.0) for x in data]
pressure=[x[5] for x in data]
volume=[(x[6]/500.0) for x in data]
#
# Use subplots to output all data as figures
#
fig, panel = plt.subplots(2,2)
#
# Plot temperature versus time
#
panel[0,0].set(xlabel='time', ylabel='temperature')
panel[0,0].scatter(time,temperature,s=0.2)
#
# Plot energy versus time
#
panel[0,1].set(xlabel='temperature', ylabel='energy per atom (eV)')
panel[0,1].scatter(temperature,energy,s=0.2)
#
# Plot pressure versus time
#
panel[1,0].set(xlabel='temperature', ylabel='pressure (bar)')
panel[1,0].scatter(temperature,pressure,s=0.2)
#
# Plot volume versus time
#
panel[1,1].set(xlabel='temperature', ylabel=r'volume per atom ($\AA^{3}$)')
panel[1,1].scatter(temperature,volume,s=0.2)

fig.set_figheight(20)
fig.set_figwidth(15)
plt.subplots_adjust(hspace=0.5)
plt.show()

