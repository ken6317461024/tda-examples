import numpy as np
import mergeSort as ms

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
                ms.mergeSort(complex[i][j])
        
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

