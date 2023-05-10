from operator import not_
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import copy
import time

class VecinosMarte(object):
    HORIZONTAL = [0, 1, 0, -1, -1, 1, 1, -1]
    VERTICAL = [-1, 0, 1, 0, -1, 1, -1, 1]

    def __init__(self, coordinates,mapMatrix,height): #constructor 
        self.coordinates = coordinates
        self.map = mapMatrix
        self.height=height

    def neighbor(self):
         #index= random.randint(0,len)
         possible_neigh=[]
         for i in range(8):
            idy = self.coordinates[0] + self.VERTICAL[i]
            idx = self.coordinates[1] + self.HORIZONTAL[i] 

            height_difference = abs(self.map[idy][idx]-self.map[self.coordinates[0]][self.coordinates[1]])
            if (self.map[idy][idx] != -1 and height_difference <= self.height):
                possible_neigh.append([idy, idx])

         index=random.randint(0,len(possible_neigh)-1)
         return VecinosMarte(possible_neigh[index],self.map,self.height)

    def getCost(self,initial_pos):
        x1=self.coordinates[1]
        y1=self.coordinates[0]
        cost1 = self.map[y1][x1]
        return cost1

# def getCost(actual_neigh,next_neigh,map):
#     x1=actual_neigh.coordinates[1]
#     y1=actual_neigh.coordinates[0]
#     x2=next_neigh.coordinates[1]
#     y2=next_neigh.coordinates[0]
#     total_cost = abs(map[y1][x1]-map[y2][x1]) #self is used so that python knows it is an object of the class
#     return total_cost

def solve(initial_pos,map,height):
    coordinates = VecinosMarte(initial_pos,map,height)
    cost=1000
    #cost = coordinates.cost()         # Initial cost    
    step = 0                     # Step count

    alpha = .9995               # Coefficient of the exponential temperature schedule        
    t0 = 1                      # Initial temperature
    t = t0    
    path_x=[]
    path_y=[]
    path_z=[]
    while step < 10000 and cost > 0:
        # Calculate temperature
        t = t0 * math.pow(alpha, step)
        step += 1
            
        # Get random neighbor
        neighbor = coordinates.neighbor()
        if neighbor==None:
           break
        new_cost = neighbor.getCost(initial_pos)

        # Test neighbor
        if new_cost < cost:
            coordinates = neighbor
            path_x.append(coordinates.coordinates[1])
            path_y.append(coordinates.coordinates[0])
            path_z.append(map[coordinates.coordinates[0]][coordinates.coordinates[1]])
            cost = new_cost
        # else:
        #     #Calculate probability of accepting the neighbor
        #     p = math.exp(-(new_cost - cost)/t)
        #     if p >= random.random():
        #         coordinates = neighbor
        #         path_x.append(coordinates.coordinates[1])
        #         path_y.append(coordinates.coordinates[0])
        #         path_z.append(map[coordinates.coordinates[0]][coordinates.coordinates[1]])
        #         cost = new_cost

        print("Iteration: ", step, "    Cost: ", cost, "    Temperature: ", t)

    print("--------Solution-----------")   
    bestCost=coordinates.getCost(initial_pos)
    print("best: ", bestCost)
    #print(initial_pos)
    print(path_z)
    return (bestCost,path_x,path_y,path_z)


it = 1
results = []
times = []
# MAIN---------------------------------------------------------#
# initial positions: x = 3350 metros y = 5800 metros
crater_map = np.load('crater_map.npy')
height=0.5

scale = 10.0174
in_x_pos = round(3350/scale)
in_y_pos =  crater_map.shape[0] - round(5800/scale)
initial_position = [in_y_pos, in_x_pos]

#------------------------------------------------------#
crater_map = np.load('crater_map.npy')
