import copy
import homology
import numpy as np
import randomPoints as rp
import vietorisRips as vr
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import datetime

start_time = datetime.now()

random = rp.randomCoordinates(10000, 2, -1000, 1000, 2)
L1 = len(random)
data1 = rp.removeRectangle(random, L1, -900, -100, -700, -100)
L2 = len(data1)
data2 = rp.removeRectangle(data1, L2, 100, 900, -900, -100)
L3 = len(data2)
data3 = rp.removeRectangle(data2, L3, -800, -450, 250, 700)
L4 = len(data3)
data = np.array(rp.removeRectangle(data3, L4, 500, 700, 500, 700))

N = 100

kmeans = KMeans(n_clusters = N)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)
centers = kmeans.cluster_centers_
centersList = [[round(centers[i][0],2),round(centers[i][1],2)] for i in range(N)]   

plt.scatter(data[:,0], data[:,1], s = 10, alpha = 0.3)
plt.scatter(centers[:,0], centers[:,1], c = 'purple', s = 200, alpha = 0.7)
plt.show()
L = [copy.deepcopy(centersList)]

epsilon = 50
i = 0

while epsilon < 510:
    
    L.append(copy.deepcopy(L[i]))
    VR = vr.vietorisRips(L[i], epsilon)
    H = homology.homology(VR)
    plt.scatter(epsilon, H[1], c = 'black')
    
    epsilon += 50
    i += 1
    
plt.show()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

