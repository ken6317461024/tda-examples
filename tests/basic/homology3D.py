import numpy as np
import itertools

def homology(numVertices,edges,faces):

    #create vertex set
    
    vertices = []
           
    for i in range(numVertices):
        vertices.append(i-1)
    
    #create sort function
    
    def swap(list,p1,p2):    
        list[p1], list[p2] = list[p2], list[p1]
        return list

    def sort(list):    
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(list)-1):
                if list[i] > list[i+1]: 
                    swap(list,i,i+1)
                    swapped = True
        return list
    
    #sort edge and face elements
    
    for i in range(len(edges)):
        sort(edges[i])
    
    for i in range(len(faces)):
        sort(faces[i])
        
    #create first order boundary operator 
        
    def bnd1(vertices,edges):
        boundary = np.zeros((len(vertices),len(edges)))
        for i in range(len(vertices)):
            for j in range(len(edges)):
                if i == min(edges[j]):
                    boundary[i][j] = -1
                if i == max(edges[j]):
                    boundary[i][j] = 1
        return boundary

    #create second order boundary operator
    
    def bnd2(edges,faces):
        boundary = np.zeros((len(edges),len(faces)))
        for i in range(len(edges)):
            for j in range(len(faces)):
                if set(edges[i]).issubset(set(faces[j])):
                    if edges[i][0] == min(faces[j]) and edges[i][1] == max(faces[j]):
                        boundary[i][j] = -1
                    else:
                        boundary[i][j] = 1
        return boundary

    def subsets(s,m):
        return set(itertools.combinations(s,m))

    if len(faces) == 0:
        
        r2 = 0
        A = bnd1(vertices,edges)
        r1 = np.linalg.matrix_rank(A)
        
    elif len(edges) == 0:
        
        r2 = 0
        r1 = 0
        
    #for i in range(len(faces)):
        #for s in subsets(faces[i],2):
            #if all(set(s) != set(edges[j]) for j in range(len(edges))):
                    #raise Exception("Not a simplex")
            
    else: 

        A, B = bnd1(vertices,edges), bnd2(edges,faces)
        r1 = np.linalg.matrix_rank(A)
        r2 = np.linalg.matrix_rank(B)
    
    H_0 = len(vertices)-r1
    H_1 = len(edges)-r1-r2
    H_2 = len(faces)-r2
    H = [H_0,H_1,H_2]
    
    return H

numVertices = 9
edges = [[0,1],[0,2],[1,2],[0,3],[1,4],[2,5],[3,4],[3,5],[4,5],[3,6],[4,7],[5,8],[6,7],[7,8],[6,8],[0,4],[1,5],[2,3],[3,7],[4,8],[5,6]]
faces = [[0,1,2],[3,4,5],[6,7,8],[0,1,4],[0,3,4],[1,2,5],[1,4,5],[0,2,3],[2,3,5],[3,6,7],[3,4,7],[4,7,8],[4,5,8],[3,5,6],[5,6,8]]

print(homology(numVertices,edges,faces))


                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    