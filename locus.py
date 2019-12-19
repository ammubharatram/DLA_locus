# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:43:03 2019

@author: BharatRamAmmu
"""


#import random
import numpy as np
m=25# take this to be odd for convenience, of having cell at the centre
matrix = np.zeros(shape=(m,m))
matrix[(m-1)//2][(m-1)//2]=1 #centre cell occupied with particle already

density_toroidal_square_list=[]
#k=1e-3 and 5e-2
#0.025,0.03,0.035,0.04,0.045,0.05
k_values=[0.05] #given stickiness paramter for the whole DLA simulation
#k=0.04
for k in k_values:

    N=100 #number of particles
    for part in range(N): #for N particles which start motion only 
        # choose cell randomly from border and place particle there, only if it is empty
        
        from my_functions import initiate_new_particle
        x_start,y_start,matrix= initiate_new_particle(m,matrix)
            
        
        #print (matrix)
        #x_old=x_start
        #y_old= y_start
        
      
        #print(matrix)
            
            
        # making old particle position empty and fill new motion particle position if there is empty place there
        no_stick=True #didn't hit yet
        iterable =0 #count number of iterations before particle stuck
        while(no_stick): #keep moving particle while it didn't stick another particle
            iterable +=1  #count number of iterations before particle stuck
            # =============================================================================
            #  move into neighbouring cell randomly : get displaced coordinates 
            # =============================================================================
            from my_functions import change_coordinates
            x_new,y_new= change_coordinates(x_start,y_start,m)
            print("This is smmoth change, non-collisional change")
            #print(matrix)
            #print(matrix[x_new,y_new])
            #print(matrix[x_new,y_new])
            
            # =============================================================================
            #          How particle moves before it sticks
            # =============================================================================
            from my_functions import move_until_it_sticks
            matrix,x_start,y_start,no_stick = move_until_it_sticks(matrix,x_new,y_new,x_start,y_start,m,k,iterable,no_stick=True) # recursive call to move until sticks
            #get old positions as starting positions for next while loop iteration
            print("The number of iterations before particle {} stuck are {}".format(part+1,iterable))

            
        
    # calculate density of matrix 
    from numpy import count_nonzero
    density_full_matrix= count_nonzero(matrix) / matrix.size
    central_matrix=matrix[(m-1)//4:(3*(m-1))//4,(m-1)//4:(3*(m-1)//4)]
    
    density_central_matrix= count_nonzero(central_matrix)/central_matrix.size
    
    density_toroidal_square= density_central_matrix-density_full_matrix
    
    print(density_toroidal_square)
    
    
    density_toroidal_square_list.append(density_toroidal_square) #add densities here
    
#density_toroidal_square_k_low005= density_toroidal_square
#density_toroidal_square_k_low05= density_toroidal_square

#
#
#
#import dill
filename= r'C:\Users\BharatRamAmmu\Documents\Locus_DLA\501X501_N50k_k0.05.pkl'
#dill.dump_session(filename)
# and to load the session again:
#dill.load_session(filename)
