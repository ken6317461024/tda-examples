import random
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter
from datetime import datetime

start_time = datetime.now()

def randomCoordinates(num, dim, lower, upper, decimals):
    
    coordinates = []
    
    for i in range(num):
        coordinates.append([])
        
    for i in range(num):
        for j in range(dim):
            coordinates[i].append(random.randint(lower*(10**decimals), upper*(10**decimals))/(10**decimals))
            
    return coordinates

random = randomCoordinates(10000, 2, -1000, 1000, 2)
L = len(random)

def removeRectangle(coordinates, size, lower, upper):

    count = 0
    j = 0 
    
    while count < size:
        if lower < coordinates[j][0] < upper and lower < coordinates[j][1] < upper:
            coordinates.remove(coordinates[j])
            count += 1
        else:
            j += 1
            count += 1
                   
    return coordinates

data = np.array(removeRectangle(random, L, -900, 900))

print("Number of points: " + str(len(data)))

plt.scatter(data[:,0], data[:,1])
plt.show()

#fig = plt.figure()
#ax = Axes3D(fig)

#for i in range(len(data)):
    #x = data[i][0]
    #y = data[i][1]
    #ax.scatter(x,y)
#plt.show()

def dist(x, y, dim):
    
    L = []
    
    for i in range(dim):
        L.append((y[i]-x[i])**2)
    
    d = math.sqrt(sum(L))
    
    return d

def mergeSortDist(alist, reference, dim):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortDist(lefthalf, reference, dim)
        mergeSortDist(righthalf, reference, dim)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if dist(lefthalf[i], reference, dim) <= dist(righthalf[j], reference, dim):
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
mergeSortDist(data, [0,0], 2)

print("sorted")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

