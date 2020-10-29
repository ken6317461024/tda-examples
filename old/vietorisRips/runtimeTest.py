import random
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
from sklearn.cluster import KMeans
import re
import shutil
import os

def randomCoordinates(num, dim, lower, upper, decimals):
    
    coordinates = []
    
    for i in range(num):
        coordinates.append([])
        
    for i in range(num):
        for j in range(dim):
            coordinates[i].append(random.randint(lower*(10**decimals), upper*(10**decimals))/(10**decimals))
            
    return coordinates

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

def VietorisRips(data, epsilon):
    
    C = []
    dim = len(data[0])
    
    for i in range(dim+1):
        C.append([])
        
    for i in range(len(data)):
        C[0].append([data[i]])
    
    while data != []:
        mergeSortDist(data, data[0], dim)
        L = len(data)
        j = 1
        while j < L:
            if dist(data[0], data[j], dim) >= epsilon:
                break
            else:
                C[1].append([data[0],data[j]])
                k = j+1
                while k < L:
                    if dist(data[0], data[k], dim) >= epsilon:
                        break
                    elif dist(data[j], data[k], dim) < epsilon:
                        C[2].append([data[0],data[j],data[k]])
                        k += 1
                    else:
                        k += 1
                j += 1   
        data.remove(data[0])
    return C

def homology(complex):
    
    cLength = len(complex)
    lengths = []
    
    for i in range(cLength):
        lengths.append(len(complex[i]))
    
    if cLength == 0:
        return "Empty"
    
    elif cLength == 1:
        return len(complex[0])
    
    else:
        
        #sort complex elements

        for i in range(cLength):
            for j in range(lengths[i]):
                mergeSort(complex[i][j])
        
        #define sublist function
                
        def sublist(lst1, lst2):
            ls = [element for element in lst1 if element in lst2]
            return ls == lst1
        
        #create boundary operators

        boundary = []
        
        for i in range(1,cLength):
            b = np.zeros((lengths[i-1],lengths[i]))
            for j in range(lengths[i-1]):
                for k in range(lengths[i]):
                    if sublist(complex[i-1][j],complex[i][k]) == True:
                        l = 0
                        for v in complex[i-1][j]:
                            w = 0
                            while True:
                                if v == complex[i][k][w]:
                                    l += w
                                    break
                                else:
                                    w += 1
                        b[j][k] = (-1)**l
            boundary.append(b)
        
        #define rank formula
        
        bLength = len(boundary)
        ranks = []
        
        for i in range(bLength):
            if boundary[i].size > 0:
                ranks.append(np.linalg.matrix_rank(boundary[i]))
            else:
                ranks.append(0)

        BettiNumbers = [lengths[0]-ranks[0]]
        
        for i in range(bLength-1):
            BettiNumbers.append(lengths[i+1]-ranks[i]-ranks[i+1])
            
        #BettiNumbers.append(lengths[-1]-ranks[-1])
            
    return BettiNumbers

def test(seed, N, epsilon):

    start_time = datetime.now()
    
    random = randomCoordinates(seed, 2, -1000, 1000, 2)
    L1 = len(random)
    data1 = removeRectangle(random, L1, -900, -100, -900, -100)
    L2 = len(data1)
    data2 = removeRectangle(data1, L2, 100, 900, -900, -100)
    L3 = len(data2)
    data3 = removeRectangle(data2, L3, -900, -100, 100, 900)
    L4 = len(data3)
    data = np.array(removeRectangle(data3, L4, 100, 900, 100, 900))
    end_time1 = datetime.now()
    
    kmeans = KMeans(n_clusters = N)
    kmeans.fit(data)
    y_kmeans = kmeans.predict(data)
    centers = kmeans.cluster_centers_
    centersList = [[round(centers[i][0],2),round(centers[i][1],2)] for i in range(N)]   
    end_time2 = datetime.now()
    
    VR = VietorisRips(centersList, epsilon)
    end_time3 = datetime.now()
    
    H = homology(VR)
    end_time4 = datetime.now()
    
    t1 = '{}'.format(end_time1 - start_time)
    t2 = '{}'.format(end_time2 - start_time)
    t3 = '{}'.format(end_time3 - start_time)
    t4 = '{}'.format(end_time4 - start_time)
    
    return t1, t2, t3, t4, H

START = datetime.now()

try:
    os.remove(r"C:\Users\kenpl\OneDrive\Documents\Programs\Results\homology.log")
except OSError:
    pass

f = open("homology.log", "w+")
print("with N=50, epsilon=500: # of initial random numbers. time to create data. time to create centers. time to create complex. time to compute homology. homology", file=open("homology.log", "a"))
f.close()

i = 1000
N = 50
epsilon = 500
Results = []

while i < 1000000: 
    
    test_i = test(i, N, epsilon)
    print(str(i) + ": " + str(test_i), file=open("homology.log", "a"))
    i += 1000

shutil.move("homology.log", r"C:\Users\kenpl\OneDrive\Documents\Programs\Results")

END1 = datetime.now()
print('Duration: {}'.format(END1 - START))

#i = 100000
#epsilon = 100

#try:
    #os.remove(r"C:\Users\kenpl\OneDrive\Documents\Programs\Results\homology2.log")
#except OSError:
    #pass

#f = open("homology2.log", "w+")
#print("with i=100000, N=50: epsilon. time to create data. time to create centers. time to create complex. time to compute homology. homology", file=open("homology2.log", "a"))
#f.close()

#while epsilon < 2000:
    
    #test_epsilon = test(i, N, epsilon)
    #print(str(epsilon) + ": " + str(test_epsilon), file=open("homology2.log", "a"))
    #epsilon += 100

#shutil.move("homology2.log", r"C:\Users\kenpl\OneDrive\Documents\Programs\Results")

#END2 = datetime.now()
#print('Duration: {}'.format(END2 - START))

#try:
    #os.remove(r"C:\Users\kenpl\OneDrive\Documents\Programs\Results\homology3.log")
#except OSError:
    #pass

#f = open("homology3.log", "w+")
#print("with i=100000, epsilon=500: # of centers. time to create data. time to create centers. time to create complex. time to compute homology. homology", file=open("homology3.log", "a"))
#f.close()

#N = 10
#epsilon = 500

#while N < 1000:

    #test_N = test(i, N, epsilon)
    #print(str(N) + ": " + str(test_N), file=open("homology3.log", "a"))
    #N += 10

#shutil.move("homology3.log", r"C:\Users\kenpl\OneDrive\Documents\Programs\Results")

#END3 = datetime.now()
#print('Duration: {}'.format(END3 - START))











































