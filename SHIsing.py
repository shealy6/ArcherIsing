# -*- codin

#!/usr/bin/env python

"""
Seán Healy
13320058

Metropolis Algorithm for Ising Model
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig

# Defining lattice size, which can be edited via the bash script
# Also defining N^2, so it doesn't happen inside any loops

N = 50
N2 = N*N

#Definining Boltzmann Constant, J (Coupling Constant), and Temperature in terms of kb and J
kb = 1
J = 1
T = 2.2692E-4
T2=T*T


# Defining a function to create an N x N lattice of integer zeroes, then randomly populating the lattice with either -1 or +1

def MakeLatt(N):
    latt = np.zeros((N,N), dtype=int)
    for i in range(N):
        for j in range(N):
            latt[i,j] = np.sign(np.random.rand()-0.5)
    return latt


latt = MakeLatt(N)
print latt


# Defining a function to return the influence of the four nearest neighbours (left, right, up, and down) in the array.
# Boundary conditions to the right and bottom of the lattice are very simply dealt with using the modulo operator and those on the left and above are dealt with explicitly
def delta_E(i,j):
# Left boundary condition
    if i==0:
		Left = latt[N-1,j]
    else:
		Left = latt[i-1,j]
		
# Upper boundary condition
    if j==0:
		Up = latt[i,N-1]
    else:
		Up = latt[i,j-1]

    return -1 * latt[i,j] * (Left + latt[(i+1)%N,j] + Up + latt[i,(j+1)%N])
    
    
"""
#Creating a function to plot the lattice as a colored grid
def grid(lattice):
    plt.matshow(lattice, cmap=plt.cm.cool)

"""

#Main Monte Carlo loop, the number of iterations is given by NIT*1000
def MonteLoop(NIT):
    
    for it in range(NIT*1000):
        i = np.random.randint(0,N)
        j = np.random.randint(0,N)
        
        d_E = J*(delta_E(i,j))
        
        # Flipping spin if energy is favourable, and then with probability Pflip if not
        if d_E >= 0:
            latt[i,j] *= -1
        elif np.exp(d_E/(kb*T)) >= np.random.rand():
            latt[i,j] *= -1
        
        #print it
        #print latt
    plt.matshow(latt, cmap=plt.cm.cool)
    plt.show     
       
"""        
        #Plotting at a number of intervals, in order to see the progression of the magnetisation through the lattice
        if it == 0:
            latt1=latt
        elif it == 10000:
            latt2=latt
        elif it == 50000:
            latt3=latt
"""            
#MonteLoop(100)      
#print latt
# Plotting the Ising Model as a coloured grid for easier visualisation

#grid(latt)
#plt.show



# Creating functions to calculate the energy and the magnetisation of the system

# Calculating the system energy
def Ecalc(latt):                     
	elatt = 0
	for i in range(N):
		for j in range(N):
			elatt += delta_E(i,j)
	return elatt/4
# The energy is divided by 4 as the contribution of each spin is counted four times as the function loops through the lattice
 
# Calculating the magnetisation of the system, summing first the rows of the arrasy, the the columns
def Mcalc(latt):				
	mag = sum(sum(latt))
	return mag
 
 
 
 
 
# The loop for extracting the Energy per Spin, Specific Heat, Magnetisation per Spin, and Magnetic Susceptibility
def MonteData(NIT):
    #Opening a text file to store the data
    #with open("data.txt", "w") as data:
    #Resetting all variables to 0
        E = E1 = EPS = SpecH = M = M1 = Mag = 0
        for it in range(NIT*1000):
            i = np.random.randint(0,N)
            j = np.random.randint(0,N)
        
            d_E = J*(delta_E(i,j))
        
            if d_E >= 0:
                latt[i,j] *= -1
            elif np.exp(2.0 * d_E/(kb*T)) >= np.random.rand():
                latt[i,j] *= -1
        
            #print it

        # Time for the system to reach equilibrium
            equil = 0
        
        # Only perform these calculations once relaxtion time has been reached
            if it > equil:
            
                # Energy Per Spin
                E = Ecalc(latt)
                E1 += E
                EPS = E1/((it-equil)*N2)	
            
                # Specific Heat
                #SpecH = ( (E**2)/(it-equil) - (E1**2)/((it-equil)**2))/(N*T2) #

                # Magnetisation per Spin, adding 0.0 is necassary to make it a float value
                #M = Mcalc(latt)
                #M1 = M1 + M
               #Mag = M1/((it-equil)) +0.0    
                
                

                # Magnetic Susceptibility
                #Msus= ( (M**2)/(it-equil) - (M1**2)/((it-equil)**2))/(N*T)  
            
                #data.write(str(it-equil) + " " + str((Mag)/N2) +'\n')
                #data.write(str((Mag)/N2) +'\n')
        return str(EPS)        
        print latt
        
#MonteData(500)
"""    
def datawrite(Ts,Te,Ti):
    with open("data.txt", "w") as data:
        MonteData()
"""        
        
print "end"