import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

vertices = [0, 1, 2, 3, 4, 5, 6]
edges = [[1,2],[1,3],[1,4],[1,5],[1,6],[0,4],[0,3],[2,3],[4,3]]

def adjmtx(matrix, matrix2):
    adjacency_matrix = np.zeros((len(vertices),len(vertices)))
    for i in range(len(vertices)):
        adjacency_matrix[i][i] = 1
        for j in range(len(vertices)):
            for k in range(len(edges)):
                if i in edges[k] and j in edges[k]:
                    adjacency_matrix[i][j] = 1
    return adjacency_matrix

A = adjmtx(vertices,edges)
G = nx.Graph()

for i in range(len(A)):
    labelmap = dict(zip(G.nodes(),[i]))
    for j in range(len(A)):
        if A[i][j] == 1:
            G.add_edges_from([(i,j)])
        
nx.draw(G, labels=labelmap, with_labels=True)

def bnd(matrix):
    boundary = np.zeros((len(A),len(edges)))
    for i in range(len(A)):
        for j in range(len(edges)):
            if i in edges[j]:
                if i == min(edges[j]):
                    boundary[i][j] = -1
                if i == max(edges[j]):
                    boundary[i][j] = 1
    return boundary

x = bnd(A).shape
r = np.linalg.matrix_rank(bnd(A))
H_0 = x[0]-r
H_1 = x[1]-r

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 20,
        }

print("Boundary Map Rank:", r)
print("Rank of H_0:", x[0]-r)
print("Rank of H_1:", x[1]-r)
plt.text(-1, 1, '$H_0(G)=Z^{}$'.format(H_0), fontdict=font)
plt.text(-1, 0.8, '$H_1(G)=Z^{}$'.format(H_1), fontdict=font)
plt.show()


