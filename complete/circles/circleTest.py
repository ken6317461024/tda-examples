import math
import random
import copy
import homology
import numpy as np
import vietorisRips as vr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from datetime import datetime

start_time = datetime.now()

u = np.random.normal(0,1,1000)
v = np.random.normal(0,1,1000)
d = (u**2+v**2)**0.5
(x,y) = (1000*(u/d),1000*(v/d))

X = x.tolist()
Y = y.tolist()
coordinates = []

for i in range(len(X)):
    coordinates.append([X[i],Y[i]])
    
for i in range(len(X)):
    coordinates.append([X[i],Y[i]])
    
data = np.array(coordinates)

end_time6 = datetime.now()
print('Duration: {}'.format(end_time6 - start_time))

N = 50
kmeans = KMeans(n_clusters = N)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)

centers = kmeans.cluster_centers_
centersList = []

for i in range(N):
    centersList.append([round(centers[i][0],2),round(centers[i][1],2)])

for i in range(len(centersList)):
    plt.scatter(centersList[i][0],centersList[i][1])
    
plt.show()
    
end_time5 = datetime.now()
print('Duration: {}'.format(end_time5 - start_time))

for i in range(len(centersList)):
    X = centersList[i][0]
    Y = centersList[i][1]
    Z = round(np.arctan(Y/X),4)
    centersList[i].append(1000*math.sin((3*Z)/2))
    centersList.append([centersList[i][0], centersList[i][1], -1000*math.sin((3*Z)/2)])

ax = plt.axes(projection='3d')

for i in range(len(centersList)):
    x = centersList[i][0]
    y = centersList[i][1]
    z = centersList[i][2]
    ax.scatter(x,y,z)
plt.show()

L = [copy.deepcopy(centersList)]

epsilon = 100
i = 0

H1 = []
H2 = []

while epsilon < 1050:
    
    L.append(copy.deepcopy(L[i]))
    VR = vr.vietorisRips(L[i], epsilon)
    H = homology.homology(VR)
    print("epsilon = " + str(epsilon) + ",  " + str(H))
    
    H1.append(H[1])
    epsilon += 50
    i += 1
    
    end_time1 = datetime.now()
    print('Duration: {}'.format(end_time1 - start_time))  

for i in range(len(H1)):
    plt.scatter(100+50*i, H1[i], c = 'red')

plt.show()    

for i in range(len(H2)):
    plt.scatter(100+50*i, H2[i], c = 'black')
    
plt.show()

end_time2 = datetime.now()
print('Duration: {}'.format(end_time2 - start_time))



