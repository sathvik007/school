#Code by GVV Sharma
#March 6, 2019
#released under GNU GPL

#This program plots the incircle of Triangle ABC
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from incentre import  icentre
#if using termux
import subprocess
import shlex
#end if


A = np.array([-2,-2]) 
B = np.array([1,3]) 
C = np.array([4,-1]) 
len = 100

p = np.zeros(2)
k1 = 1
k2 = 1
I,r = icentre(A,B,C,k1,k2)
x1 = I+r
D = perp_foot(I,B,C)
E = perp_foot(I,C,A)
F = perp_foot(I,A,B)
x1 = I+get_coord(r,3*np.pi/2-np.pi/9)
x2 = circ_chord(C-A,x1,I)
print(A,B,C,D,E,F,I,r,x1,x2)
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + I).T

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$incircle$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 - 0.1) , 'I')
plt.plot(x1[0], x1[1], 'o')
plt.text(x1[0] * (1 + 0.1), x1[1] * (1 - 0.1) , 'x1')
plt.plot(x2[0], x2[1], 'o')
plt.text(x2[0] * (1 + 0.1), x2[1] * (1 - 0.1) , 'x2')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/incircle.pdf')
plt.savefig('../figs/incircle.eps')
subprocess.run(shlex.split("termux-open ../figs/incircle.pdf"))
#else
#plt.show()


