import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def homology(adjacency_matrix):
    
    edges = []
    G = nx.Graph()
    
    for i in range(len(adjacency_matrix)):
        labelmap = dict(zip(G.nodes(),[i]))
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                G.add_edges_from([(i,j)])
                if i<j:
                    edges.append([i,j])
            
    nx.draw(G, labels=labelmap, with_labels=True)
    
    def bnd(matrix):
        boundary = np.zeros((len(adjacency_matrix),len(edges)))
        for i in range(len(adjacency_matrix)):
            for j in range(len(edges)):
                if i in edges[j]:
                    if i == min(edges[j]):
                        boundary[i][j] = -1
                    if i == max(edges[j]):
                        boundary[i][j] = 1
        return boundary
    
    x = bnd(adjacency_matrix).shape
    r = np.linalg.matrix_rank(bnd(adjacency_matrix))
    H_0 = x[0]-r
    H_1 = x[1]-r
    H = [H_0,H_1]
    
    font = {'family': 'serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 20,
            }
    
    plt.text(-1, 1, '$H_0(G)=Z^{}$'.format(H_0), fontdict=font)
    plt.text(-1, 0.8, '$H_1(G)=Z^{}$'.format(H_1), fontdict=font)

    return H


A = [[1,0,1,0,1,1],[0,1,0,1,1,1],[1,0,1,0,0,1],[0,1,0,1,1,0],[1,1,0,1,0,0],[1,1,1,0,0,1]]

print('Rank of H(G):', homology(A))

