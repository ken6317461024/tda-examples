import random
import math
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

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

random = randomCoordinates(1000, 2, -1000, 1000, 2)
L1 = len(random)
data1 = removeRectangle(random, L1, -900, -100, -700, -100)
L2 = len(data1)
data2 = removeRectangle(data1, L2, 100, 900, -900, -100)
L3 = len(data2)
data3 = removeRectangle(data2, L3, -800, -450, 250, 700)
L4 = len(data3)
data = np.array(removeRectangle(data3, L4, 500, 700, 500, 700))

N=5

while N<200:

    N += 5

    kmeans = KMeans(n_clusters = N)
    kmeans.fit(data)
    y_kmeans = kmeans.predict(data)
    centers = kmeans.cluster_centers_
    centersList = [[round(centers[i][0],2),round(centers[i][1],2)] for i in range(N)]   

    print(str(N) + ": " + str(silhouette_score(data,kmeans.labels_))) 

