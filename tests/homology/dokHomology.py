from scipy.sparse import dok_matrix
from scipy.sparse.linalg import svds, eigs

def homology(simplicialComplex):
    
    cLength = len(simplicialComplex)
    lengths = []
    
    for i in range(cLength):
        lengths.append(len(simplicialComplex[i]))
    
    if cLength == 0:
        return "Empty"
    
    elif cLength == 1:
        return len(simplicialComplex[0])
    
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
                    if sublist(simplicialComplex[i-1][k],simplicialComplex[i][j]) == True:
                        b[k,j] = l
                        l *= -1
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

        BettiNumbers = [len(simplicialComplex[0])-ranks[0]]
        
        for i in range(bLength-1):
            BettiNumbers.append(len(simplicialComplex[i+1])-ranks[i]-ranks[i+1])
                
            BettiNumbers.append(len(simplicialComplex[-1])-ranks[-1])
            
    return BettiNumbers

