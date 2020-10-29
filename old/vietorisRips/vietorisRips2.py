import numpy as np
import math
import itertools

def dist(x, y, dim):
    
    L = []
    
    for i in range(dim):
        L.append((y[i]-x[i])**2)
    
    d = math.sqrt(sum(L))
    
    return d

def mergeSortX(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortX(lefthalf)
        mergeSortX(righthalf)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] <= righthalf[j][0]:
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
    
    C = []
    dim = len(data[0])
    
    mergeSortX(data)
    
    print(data)
    
    for i in range(dim+1):
        C.append([])
        
    for i in range(len(data)):
        C[0].append([data[i]])
    
    for i in range(2,dim+2):
        
        for j in range(len(data)):
            k=j+1
            while k > j:
                if k > len(data):
                    break
                elif abs(data[k] - data[j]) > epsilon:
                    break
                else:
                    C[1].append([data[j],data[k]])
            
                
        
        subsets = [list(i) for i in itertools.combinations(data,i)]
        near = []
        
        for j in range(len(subsets)):
            for k in range(len(subsets[0])):
                for n in range(k+1,len(subsets[0])):
                    if dist(subsets[j][k], subsets[j][n], dim) < epsilon:
                        near.append(True)
                    else:
                        near.append(False)
            
            if all(near):
                C[i-1].append(subsets[j])
    
    return C

data = [[1,2],[2,3],[0,0],[-1,5]]
epsilon = 10

VR = VietorisRips(data,epsilon)

print(len(data))
print(VR[1])
print(len(VR[1]))
print(VR[2])
print(len(VR[2]))



