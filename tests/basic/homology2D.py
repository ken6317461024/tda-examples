import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def homology(numVertices,edges):
    
    vertices = []
    
    for i in range(numVertices):
        vertices.append(i-1)
    
    def adjmtx(vertices, edges):
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
    H = [H_0,H_1]    
    
    font = {'family': 'serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 20,
            }

    plt.text(-1, 1, 'rank$(H_0(G))={}$'.format(H_0), fontdict=font)
    plt.text(-1, 0.8, 'rank$(H_1(G))={}$'.format(H_1), fontdict=font)

    return H

numVertices = 9
edges = [[0,1],[0,2],[1,2],[0,3],[1,4],[2,5],[3,4],[3,5],[4,5],[3,6],[4,7],[5,8],[6,7],[7,8],[6,8],[0,4],[1,5],[2,3],[3,7],[4,8],[5,6]]

print('Rank of H(G):',homology(numVertices,edges))

