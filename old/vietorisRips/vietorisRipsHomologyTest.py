import random
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt
from collections import Counter

def randomCoordinates(num, dim, lower, upper, decimals):
    
    coordinates = []
    
    for i in range(num):
        coordinates.append([])
        
    for i in range(num):
        for j in range(dim):
            coordinates[i].append(random.randint(lower*(10**decimals), upper*(10**decimals))/(10**decimals))
            
    return coordinates

random = randomCoordinates(50, 2, -1000, 1000, 2)
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

data = removeRectangle(random, L, -600, 600)

print("Number of points: " + str(len(data)))

for i in range(len(data)):
    x = data[i][0]
    y = data[i][1]
    plt.scatter(x,y)
plt.show()

def dist(x, y, dim):
    
    L = []
    
    for i in range(dim):
        L.append((y[i]-x[i])**2)
    
    d = math.sqrt(sum(L))
    
    return d

def VietorisRips(data, epsilon):
    
    C = []
    dim = len(data[0])
    
    for i in range(dim+1):
        C.append([])
        
    for i in range(len(data)):
        C[0].append([data[i]])
    
    for i in range(2,dim+2):
        
        subsets = [list(i) for i in itertools.combinations(data,i)]
        near = []
        
        for j in range(len(subsets)):
            for k in range(len(subsets[0])):
                for n in range(k+1,len(subsets[0])):
                    if dist(subsets[j][k], subsets[j][n], dim) < epsilon:
                        near.append(True)
        
            if all(near):
                C[i-1].append(subsets[j])
    
    return C

epsilon = 1

VR = VietorisRips(data,epsilon)

def homology(complex):
    
    #create sort function
    
    if len(complex) == 0:
        return "Empty"
    
    elif len(complex) == 1:
        return len(complex[0])
    
    else:
        
    #create sort function
    
        def swap(list,p1,p2):    
            list[p1], list[p2] = list[p2], list[p1]
            return list
    
        def sort(list):    
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(list)-1):
                    if list[i] > list[i+1]: 
                        swap(list,i,i+1)
                        swapped = True
            return list        
        
        #sort complex elements
        
        for i in range(len(complex)):
            for j in range(len(complex[i])):
                sort(complex[i][j])

        #define sublist function
                
        def sublist(lst1, lst2):
            ls = [element for element in lst1 if element in lst2]
            return ls == lst1
        
        #create boundary operators

        def bnd(complex):
            boundary = []
            for i in range(1,len(complex)):
                b = np.zeros((len(complex[i-1]),len(complex[i])))
                for j in range(len(complex[i-1])):
                    for k in range(len(complex[i])):
                        if sublist(complex[i-1][j],complex[i][k]) == True:
                            l = 0
                            for v in complex[i-1][j]:
                                for w in range(len(complex[i][k])):
                                    if v == complex[i][k][w]:
                                        l += w
                            b[j][k] = (-1)**l
                boundary.append(b)
            return boundary

        ranks = []
        
        for i in range(len(bnd(complex))):
            ranks.append(np.linalg.matrix_rank(bnd(complex)[i]))

        BettiNumbers = [len(complex[0])-ranks[0]]
        
        for i in range(len(bnd(complex))-1):
            BettiNumbers.append(len(complex[i+1])-ranks[i]-ranks[i+1])
            
        #BettiNumbers.append(len(complex[-1])-ranks[-1])
            
    return BettiNumbers

print(homology(VR))

