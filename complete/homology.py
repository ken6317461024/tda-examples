import numpy as np
import itertools
from scipy.sparse import dok_matrix
from scipy.sparse.linalg import svds, eigs

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

        #define sublist function
                
        def sublist(lst1, lst2):
            ls = [element for element in lst1 if element in lst2]
            return ls == lst1
        
        #create boundary operators


        boundary = []
        for i in range(1,cLength):
            b = dok_matrix((lengths[i-1],lengths[i]))
            for j in range(lengths[i]):
                l = -1
                for k in range(lengths[i-1]):
                    if sublist(complex[i-1][k],complex[i][j]) == True:
                        b[k,j] = l
                        l *= -1
            print("Size of operator " + str(i) + " = " + str(len(b)))
            boundary.append(b)

        bLength = len(boundary)
        
        #define rank formula
        
        def rank(A, eps=1e-12):
            u, s, vh = svds(A, k=3)
            return len([x for x in s if abs(x) > eps])
        
        ranks = []
        
        for i in range(bLength):
            if boundary[i].size > 0:
                ranks.append(rank(boundary[i]))
            else:
                ranks.append(0)

        BettiNumbers = [len(complex[0])-ranks[0]]
        
        for i in range(bLength-1):
            BettiNumbers.append(len(complex[i+1])-ranks[i]-ranks[i+1])
            
        BettiNumbers.append(len(complex[-1])-ranks[-1])
            
    return BettiNumbers

s0 = [[0],[1],[2],[3]]
s1 = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
s2 = [[0,1,2],[0,1,3],[1,2,3],[0,2,3]]
C = [s0,s1,s2]

print(homology(C))


