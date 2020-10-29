import numpy as np
import itertools
from collections import Counter

def homology(complex):
    
    #create sort function
    
    if len(complex) == 0:
        return "Empty"
    
    elif len(complex) == 1:
        return len(complex[0])
    
    else:
        
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
        
        #sort complex elements
        
        for i in range(len(complex)):
            for j in range(len(complex[i])):
                sort(complex[i][j])

        #define sublist function
                
        def sublist(lst1, lst2):
            ls = [element for element in lst1 if element in lst2]
            return ls == lst1
        
        #create boundary operators

        def bnd(complex):
            boundary = []
            for i in range(1,len(complex)):
                b = np.zeros((len(complex[i-1]),len(complex[i])))
                for j in range(len(complex[i-1])):
                    for k in range(len(complex[i])):
                        if sublist(complex[i-1][j],complex[i][k]) == True:
                            l = 0
                            for v in complex[i-1][j]:
                                for w in range(len(complex[i][k])):
                                    if v == complex[i][k][w]:
                                        l += w
                            b[j][k] = (-1)**l
                boundary.append(b)
            return boundary

        ranks = []
        
        for i in range(len(bnd(complex))):
            ranks.append(np.linalg.matrix_rank(bnd(complex)[i]))

        BettiNumbers = [len(complex[0])-ranks[0]]
        
        for i in range(len(bnd(complex))-1):
            BettiNumbers.append(len(complex[i+1])-ranks[i]-ranks[i+1])
            
        BettiNumbers.append(len(complex[-1])-ranks[-1])
            
    return BettiNumbers

s0 = [[0],[1],[2],[3]]
s1 = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
s2 = [[0,1,2],[0,1,3],[1,2,3],[0,2,3]]
C = [s0,s1,s2]

print(homology(C))


