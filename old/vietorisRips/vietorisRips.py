import numpy as np
import math
import itertools

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
                    else:
                        near.append(False)
            
            if all(near):
                C[i-1].append(subsets[j])
    
    return C

data = [[1,2],[2,2],[0,2]]
epsilon = 1

VR = VietorisRips(data,epsilon)

print(len(data))
print(VR[1])
print(len(VR[1]))
print(VR[2])
print(len(VR[2]))



