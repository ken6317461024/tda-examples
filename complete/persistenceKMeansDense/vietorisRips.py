import math
import mergeSort as ms

def vietorisRips(data, epsilon):
    
    C = []
    dim = len(data[0])
    
    for i in range(dim+1):
        C.append([])
        
    for i in range(len(data)):
        C[0].append([data[i]])
    
    while data != []:

        ms.mergeSortDist(data, data[0], dim)
        L = len(data)
        j = 1

        while j < L:

            if ms.dist(data[0], data[j], dim) >= epsilon:
                break

            else:
                C[1].append([data[0],data[j]])
                k = j+1

                while k < L:
                    
                    if ms.dist(data[0], data[k], dim) >= epsilon:
                        break

                    elif ms.dist(data[j], data[k], dim) < epsilon:
                        C[2].append([data[0],data[j],data[k]])
                        k += 1

                    else:
                        k += 1

                j += 1   

        data.remove(data[0])

    return C

