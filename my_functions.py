# -*- coding: utf-8 -*-
# =============================================================================
# Module Level variables
# =============================================================================


sticked = None
filled=None
filled_stick=None




"""
Input
x: existing x-coordinate of particle
y_new: existing y-coordinate of particle
m : dimensions of the matrix
"""

import numpy as np
import random
from random import choices

def change_coordinates(x,y,m):
    
    # =============================================================================
    # Moving the collided particle randomly to neighboruing cells like earlier
    # =============================================================================
    x_motion = x+ np.random.choice([-1,0,1])
    if x_motion == x:  # if new x-position doesn't change, ensure new y- position changes for sure- no 0
        y_motion = y+ np.random.choice([-1,1]) 
    else: # if x-position changed, y-position can but need not change - hence -1,0,1 (including 0)
        y_motion = y+ np.random.choice([-1,0,1])   
    print("coordinates are now changed")
    #for particle being in border, account for toroidal bounding or bouncing: particle either bounces little or much
    # (0,m-1): 0 and m-1 refer to toroidal bounding respecitively for both conditions
    # other values refer to bouncing randomly
    
    # account for toroidal bounding
    #if coordinate exceeds the last row/column, it goest to first row/column respectively
    if x_motion<0:
        x_motion = m-1
    if y_motion<0:
        y_motion = m-1
    if x_motion>m-1:
        x_motion = 0 #if coordinate exceeds the last row/column, it goest to first row/column respectively
    if y_motion>m-1:
        y_motion= 0
    #print(matrix)
    #print(matrix[x_motion,y_motion])
    # Updated coordinates of particle
    x_updated= x_motion
    y_updated = y_motion
    return (x_updated,y_updated)


"""
Input
k: stickiness probability
Output
stick_flag: 0 or 1 indicating it stuck or not
stick_flag_text: text indicating it stuck or not
"""

def stickiness_choice(k):
    population = [0,1]
    weights=[1-k,k]
    stick_flag=choices(population, weights)#get a random sample, following given probability distribution of population
    stick_flag_text= np.where(stick_flag==[0],'did not stick','stuck')
    print('The particle {}'.format(stick_flag_text))
    return (stick_flag,stick_flag_text)



"""
Input
x_new,y_new: new coordinates of particle 
x_start,y_start: starting coordinates of particle, before iteration started
matrix= input matrix
m = dimensions of square matrix
no_stick= flag whether it stuck or not


Output

gives updated matrix, updated old coordinates for next while loop iteration and final coordinates of that particle
"""


def move_until_it_sticks(matrix,x_new,y_new,x_start,y_start,m,k,iterable,no_stick=True):
    # =============================================================================
    #  while this new position is empty /not occupied or particle did not stick: move to new coordinates
    # =============================================================================
    
    
    
    stuck_moved= False  #when particle stuck and moved to another position, we don't repeat while loop
    while(stuck_moved==False):
        
        if matrix[x_new,y_new]!=1: #while this new position is empty /not occupied
                matrix
                matrix[x_start,y_start]=0 #remove particle from old or starting position
                matrix[x_new,y_new]=1 #place particle in new motion position
                x_old = x_new #change motion coordinates to old coordinates, for while loop to restart
                y_old= y_new #change motion coordinates to old coordinates, for while loop to restart
                # motion particle becomes old particle for next iteration!
                print("particle occupied empty position")
                iterable+=1 #this is one iteration
                stuck_moved= True
                break
                    
        elif matrix[x_new,y_new]==1:
                stuck_moved = False
                # =============================================================================
                # Check once it hits, it sticks or not based on sticking probability 'k'
                # =============================================================================
                print("Particle hit another particle, but let's see if it sticks!")
                from my_functions import stickiness_choice
                stick_flag,stick_flag_text = stickiness_choice(k) #written in my_functions
                
                # =============================================================================
                # If it didn't stick, repeat the process of moving to new coordinates
                # =============================================================================
                if (stick_flag==[0]):
                    from my_functions import change_coordinates
                    x_old= x_new
                    y_old= y_new
                    x_new,y_new = change_coordinates(x_new,y_new,m)   #updated coordinates after movement              
                    
                    stuck_moved = False #recurse with updated coordinates
                    
                    
                # =============================================================================
                #         the particle stuck with another particle
                # =============================================================================
                else: # meaning the particle stuck with another particle
                    #x_finish = x_start
                    #y_finish = y_start
                    #matrix[x_start,y_start]=0 #remove particle from old position, which is starting position
                    #matrix[x_finish,y_finish]=1 #stick particle to existing particles
                     #stick particle to existing particles- let it be in old position- x_start
                    #stick_particle(m,matrix,x_new,y_new,x_start,y_start)
                    x_old = x_new
                    y_old= y_new
                    stuck_moved = True #stop internal while loop, as particle now stuck
                    no_stick= False #stop the bigger while loop using this global variable, as particle now stikcs
                    
    return (matrix,x_old,y_old,no_stick)

def initiate_new_particle(m,matrix):
    filled=True
    while (filled==True):
        
        x_start= random.randint(0,m-1)
            
        if x_start in (0,m-1):
            
            y_start= random.randint(0,m-1)
        else:
            
            y_start= random.choice([0,m-1])
        print(x_start,y_start)
        print(matrix[x_start,y_start])
        if (matrix[x_start,y_start]==0): #if it is empty, take that place
            print('empty cell found')
            
            filled= False
            print("filled flag is now {}".format(filled))
            matrix[x_start,y_start]=1
            return x_start,y_start,matrix
            continue
        else:                           # if occupied, try initiating in another place, again in the border
            
            filled= True                   # while loop repeats, hence initiation restarts
            print("filled flag is now {}".format(filled))
            print("initiation restarts")
       
        
    

def stick_particle(m,matrix,x_new,y_new,x_start,y_start):
    filled_stick=True
    while (filled_stick):
        x_finish = x_new+ np.random.choice([-1,0,1])
        if x_finish == x_new:  # if new x-position doesn't change, ensure new y- position changes for sure- no 0
            y_finish = y_new+ np.random.choice([-1,1]) 
        else: # if x-position changed, y-position can but need not change - hence -1,0,1 (including 0)
           y_finish = y_new+ np.random.choice([-1,0,1]) 
    
    
        # =============================================================================
        #    for particle sticking another which is in border, it can stick in less sides
        # =============================================================================
        if x_finish<0 and y_finish!=y_new: #<0 happens when x_new =0
            x_finish =np.random.choice([0,1])
        if x_finish<0 and y_finish==y_new:
            x_finish =1 #as it can't be in same cell as hitting particle as x_new=0
           
        if x_finish>m-1 and y_finish!=y_new: #<m-1 happens when x_new =m-1
            x_finish=np.random.choice([m-2,m-1])
        if x_finish>m-1 and y_finish==y_new:
            x_finish=m-2 #as it can't be in same cell as hitting particle
            
        
        if y_finish<0 and x_finish!=x_new:
             y_finish = np.random.choice([0,1])
        if y_finish<0 and x_finish==x_new:
            y_finish=1 #as it can't be in same cell as hitting particle
            
            
        if y_finish>m-1 and x_finish!=x_new:
            y_finish=np.random.choice([m-2,m-1]) 
        if y_finish>m-1 and x_finish==x_new:
            y_finish=m-2 #as it can't be in same cell as hitting particle
        
        print(x_finish,y_finish)
        print(matrix[x_finish,y_finish])
        # =============================================================================
        # moving particle from initial to final position
        # =============================================================================
        if matrix[x_finish,y_finish]==0: #if it is empty, take that place around neighborhood to stuck particle
            
            filled_stick= False
            matrix[x_start,y_start]=0 #remove particle from old position, which is starting position
            matrix[x_finish,y_finish]=1 #stick particle to existing particles
            print("Sticked particle in neighborhood of collided particle")
            break
        
        else:                       # if particle exists, repeat sticking location in some other position within neighborhood of particle itself
            
            filled_stick= True # repeat to stick in an empty neighboring cell
            print("can't stick it here, look for another sticking coordinates")
            
