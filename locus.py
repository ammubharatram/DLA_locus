# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:43:03 2019

@author: BharatRamAmmu
"""


import random
import numpy as np
m=51 # take this to be odd for convenience, of having cell at the centre
matrix = np.zeros(shape=(m,m))
matrix[(m-1)//2][(m-1)//2]=1

part =0 #initiate particle count, start with 
#k=1e-3 and 5e-2
k_values=[0.001,0.005,0.01,0.015,0.02,0.05] #given stickiness paramter for the whole DLA simulation
k = k_values[1]
N=1000
for part in range(N): #for 100 particles which start motion only 
    # choose cell randomly from border and place particle there
    x_start= random.randint(0,m-1)
    
    if x_start in (0,m-1):
        y_start= random.randint(0,m-1)
    else:
        y_start= random.choice([0,m-1])
    #print (x_start,y_start)
    matrix[x_start,y_start]=1
    #x_old=x_start
    #y_old= y_start
    
  
    #print(matrix)
        
        
    # making old particle position empty and fill new motion particle position if there is empty place there
    no_stick=True #didn't hit yet
    iterable =0 #count number of iterations before particle stuck
    while(no_stick): #keep moving particle while it didn't stick another particle
        iterable +=1 
        
        # =============================================================================
        #  move into neighbouring cell randomly : get displaced coordinates 
        # =============================================================================
        x_new = x_start+ np.random.choice([-1,0,1])
        if x_new == x_start:  # if new x-position doesn't change, ensure new y- position changes for sure- no 0
            y_new = y_start+ np.random.choice([-1,1]) 
        else: # if x-position changed, y-position can but need not change - hence -1,0,1 (including 0)
            y_new = y_start+ np.random.choice([-1,0,1])   
        
        #for particle being in border, account for toroidal bounding or bouncing: particle either bounces little or much
        # (0,m-1): 0 and m-1 refer to toroidal bounding respecitively for both conditions
        # other values refer to bouncing randomly
        if x_new<0 or x_new>m-1:
            x_new = random.choice([0,m-1])
        if y_new<0 or y_new>m-1:
            y_new = random.choice([0,m-1])
        #print(matrix)
        #print(matrix[x_new,y_new])
        print(matrix[x_new,y_new])
        
        # =============================================================================
        #          How particle moves before it sticks
        # =============================================================================
        from my_functions import move_until_it_sticks
        matrix,x_start,y_start,no_stick = move_until_it_sticks(matrix,x_new,y_new,x_start,y_start,m,k,iterable,no_stick=True) # recursive call to move until sticks
        
        
       
    part+=1 #now iterate for a new upcoming particle,once this particle sticks
        #
            
        
# calculate density of matrix 
from numpy import count_nonzero
density_full_matrix= count_nonzero(matrix) / matrix.size
central_matrix=matrix[(m-1)//4:(3*(m-1))//4,(m-1)//4:(3*(m-1)//4)]

density_central_matrix= count_nonzero(central_matrix)/central_matrix.size

density_toroidal_square= density_full_matrix-density_central_matrix

print(density_toroidal_square)


density_toroidal_square #for minium k -

density_toroidal_square_k_low005= density_toroidal_square
#density_toroidal_square_k_low05= density_toroidal_square

#
#
#
#import dill
#filename= r'C:\Users\BharatRamAmmu\Documents\Locus_DLA\501X501_N50k_k0.05.pkl'
#dill.dump_session(filename)
## and to load the session again:
#dill.load_session(filename)