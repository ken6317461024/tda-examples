import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

random = randomCoordinates(10, 2, -1000, 1000, 2)
L1 = len(random)

def removeRectangle(coordinates, size, lower1, upper1, lower2, upper2):

    count = 0
    j = 0 
    
    while count < size:
        if lower1 < coordinates[j][0] < upper1 and lower2 < coordinates[j][1] < upper2:
            coordinates.remove(coordinates[j])
            count += 1
        else:
            j += 1
            count += 1
                   
    return coordinates

data1 = removeRectangle(random, L1, -900, -100, -900, -100)
L2 = len(data1)
data2 = removeRectangle(data1, L2, 100, 900, -900, -100)
L3 = len(data2)
data3 = removeRectangle(data2, L3, -900, -100, 100, 900)
L4 = len(data3)
data = removeRectangle(data3, L4, 100, 900, 100, 900)

print("Number of points: " + str(len(data)))

#fig = plt.figure()
#ax = Axes3D(fig)

for i in range(len(data)):
    x = data[i][0]
    y = data[i][1]
    plt.scatter(x,y)
plt.show()

#for i in range(len(data)):
    #x = data[i][0]
    #y = data[i][1]
    #z = data[i][2]
    #ax.scatter(x,y,z)
#plt.show()

def mergeSort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
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

def dist(x, y, dim):
    
    L = [(y[i]-x[i])**2 for i in range(dim)]
    d = math.sqrt(sum(L))
    
    return d

def dist2(X, x, dim):
    
    L = [dist(x,y,dim) for y in X]

    return L
    
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

def VietorisRips(data, epsilon):
    
    dim = len(data[0])
    C = []
    C = [[] for i in range(dim+1)]
    C[0] = [[data[i]] for i in range(len(data))]
    
    while data != []:
        mergeSortDist(data, data[0], dim)
        L = len(data)
        j = 1 
        while j < L:
            X = [data[0]]
            if dist(data[0], data[j], dim) >= epsilon:
                break
            else:
                C[1].append([data[0],data[j]])
                i = 2
                X.append(data[j])
                print(X)
                n = j
                k = n+1
                while True:
                    print(str(k))
                    if i >= dim or k >= L:
                        i -= 1
                        n += 1
                        k = n+1
                    if dist(data[0], data[k], dim) >= epsilon:
                        i -= 1
                        n += 1
                        k = n+1
                    elif i < 2:
                        break
                    elif all(dist2(X, data[k], dim)[n] < epsilon for n in range(len(X))):
                        X.append(data[k])
                        C[i].append(X)
                        i += 1
                        k += 1
                    else:
                        k += 1
            j += 1
        data.remove(data[0])
        
    return C

epsilon = 5000

VR = VietorisRips(data, epsilon)

print("Number of edges: " + str(len(VR[1])))
print("Number of faces: " + str(len(VR[2])))

end_time1 = datetime.now()
print('Duration: {}'.format(end_time1 - start_time))

#data = [[1,2],[2,3],[0,0],[-1,5]]
#epsilon = 2

#VR = VietorisRips(data,epsilon)

#print(len(data))
#print(VR[1])
#print(len(VR[1]))
#print(VR[2])
#print(len(VR[2]))



