import numpy as np

def rowSwap(matrix,a,b):
    
    shape = np.matrix(matrix).shape
    copy = np.copy(matrix)

    for i in range(shape[1]):
        matrix[a][i] = copy[b][i]
        matrix[b][i] = copy[a][i]
        
    matrix = np.matrix(matrix)
    
    return matrix
    
def colSwap(matrix,a,b):
    
    shape = np.matrix(matrix).shape
    copy = np.copy(matrix)

    for i in range(shape[0]):
        matrix[i][a] = copy[i][b]
        matrix[i][b] = copy[i][a]
        
    matrix = np.matrix(matrix)
    
    return matrix

def scaleCol(matrix,col,scale):
    
    shape = np.matrix(matrix).shape
    
    for i in range(shape[0]):
        matrix[i][col] = scale*matrix[i][col]
        
    matrix = np.matrix(matrix)
        
    return matrix

def scaleRow(matrix,row,scale):
    
    shape = np.matrix(matrix).shape
    
    for i in range(shape[1]):
        matrix[row][i] = scale*matrix[row][i]
        
    matrix = np.matrix(matrix)
        
    return matrix

def rowCombine(matrix,row1,row2,scale):
    
    shape = np.matrix(matrix).shape
    copy = np.copy(matrix)
    
    for i in range(shape[1]):
        matrix[row1][i] = matrix[row1][i]+scale*copy[row2][i]
        
    matrix = np.matrix(matrix)
    
    return matrix

def colCombine(matrix,col1,col2,scale):
    
    shape = np.matrix(matrix).shape
    copy = np.copy(matrix)
    
    for i in range(shape[0]):
        matrix[i][col1] = matrix[i][col1]+scale*copy[i][col2]
        
    matrix = np.matrix(matrix)
    
    return matrix

def transpose(matrix):
        
    copy = np.copy(matrix)
    transpose = np.zeros((copy.shape[1],copy.shape[0]))
        
    for i in range(copy.shape[1]):
        for j in range(copy.shape[0]):
            transpose[i][j] = matrix[j][i]
                
    return transpose

def simReduce(matrix1, matrix2):
        
    numRows, numCols = np.matrix(matrix1).shape
    i,j = 0,0
        
    while True:
        
        if i >= numRows or j >= numCols:
            break
            
        if matrix1[i][j] == 0:
            nonzeroCol = j
                
            while nonzeroCol < numCols and matrix1[i][nonzeroCol] == 0:
                nonzeroCol += 1
            
            if nonzeroCol == numCols:
                i += 1
                continue
                
            colSwap(matrix1,j,nonzeroCol)
            rowSwap(matrix2,j,nonzeroCol)
                
        pivot = matrix1[i][j]
        scaleCol(matrix1, j, 1.0/pivot)
        scaleRow(matrix2, j, 1.0/pivot)
            
        for otherCol in range(0, numCols):
            if otherCol == j:
                continue
            if matrix1[i][otherCol] != 0:
                scale = -matrix1[i,otherCol]
                colCombine(matrix1, otherCol, j, scale)
                rowCombine(matrix2, j, otherCol, -scale)
                    
        i += 1
        j += 1
        
    return matrix1, matrix2
    
A = [[1,2],[3,4]]

print(np.matrix(A))
print(rowSwap(A,0,1))
print(colSwap(A,0,1))
print(scaleCol(A,0,2))
print(scaleRow(A,0,2))
print(rowCombine(A,0,1,2))
print(colCombine(A,0,1,2))





























