from operator import not_
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import copy
import time

points_coordinates = np.array(pd.read_csv('in.csv', delimiter=',', header=None))

# TODO 
# Moving connections of points in the plot
print(points_coordinates)
print(points_coordinates[0])
moves = []

class PointsGraph(object):

    def __init__(self, points):
        self.points = copy.deepcopy(points)
        self.length = len(points)

    def neighbor(self):
        aux_neighbor = PointsGraph(self.points)

        id1 = np.random.randint(0, self.length)
        id2 = np.random.randint(0, self.length)

        while id2 == id1:
            id2 = np.random.randint(0, self.length)

        aux_neighbor.points[id1] = self.points[id2]
        aux_neighbor.points[id2] = self.points[id1]

        return aux_neighbor

    def cost(self):
        total_cost = 0
        for i in range(self.length-1):
            point_a = self.points[i]
            point_b = self.points[i+1]

            total_cost = total_cost + self.distance(point_a, point_b)

        total_cost = total_cost + self.distance(self.points[0], self.points[-1])

        return total_cost

    def distance(self, a, b):
        x2 = a[0]
        x1 = b[0]

        y2 = a[1]
        y1 = b[1]

        return ((x2-x1)**2 + (y2-y1)**2)**(1/2)

    def show(self):
        for i in range(self.length):
            print(self.points[i])

def solve(points_coordinates):
    points = PointsGraph(points_coordinates)

    cost = points.cost()         # Initial cost    
    step = 0                     # Step count

    alpha = .9995               # Coefficient of the exponential temperature schedule        
    t0 = 1                      # Initial temperature
    t = t0    

    while step < 10000 and cost > 0:

        # Calculate temperature
        t = t0 * math.pow(alpha, step)
        step += 1
            
        # Get random neighbor
        neighbor = points.neighbor()
        new_cost = neighbor.cost()

        # Test neighbor
        if new_cost < cost:
            points = neighbor
            cost = new_cost
        else:
            # Calculate probability of accepting the neighbor
            p = math.exp(-(new_cost - cost)/t)
            if p >= random.random():
                points = neighbor
                cost = new_cost

        print("Iteration: ", step, "    Cost: ", cost, "    Temperature: ", t)

    # print("--------Solution-----------")   
    # # board.show()
    print("best: ", points.cost())

    return points.cost()


it = 100
results = []
times = []


for i in range(it):
    start_time = time.time()
    res = solve(points_coordinates)
    times.append(time.time() - start_time)
    results.append(res)

print("Stats para cacminata simple")
print(f'Avg. de longitudes: {np.mean(results):.4f} metros')
print(f'Avg. de tiempos de ejecucion: {np.mean(times):.4f} seconds')

# print(best_sol.cost())
# best_sol.show()
# x, y = np.split(points.points, 2, axis = 1)

# x = np.append(x, x[0])
# y = np.append(y, y[0])

# print(x)
# print(y)

# plt.plot(x, y)
# plt.show()