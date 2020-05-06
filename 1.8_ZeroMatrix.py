#--------------------------------------------------
# If an element in an MxN matrix is 0, its entire row and
# column are set to 0.
#--------------------------------------------------
'''
Todo:
  1. Figure out np.matrix index, am I correct way? mat[1,:][:,1] = arr[1][1]
  
Hint:
  1. Find zero part first
  2. Use only O(n) for extra space
  3. Use original matrix to remember info

Note:

'''

import numpy as np


DEBUG = 0
def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def zeroMatrix_1st_list(mat):
    ''' Complexity: O(N^2) / O(N^2) '''
    row = len(mat)
    col = len(mat[0])

    # Declaire new 2d array based on original 2d array
    retMat = [[0 for c in range(col)] for r in range(row)]

    # Copy 2d array
    for r in range(row):
        for c in range(col): 
            retMat[r][c] = mat[r][c]

    # Set corresponding row and col to 0
    for r in range(row):
        for c in range(col):            
            if mat[r][c] == 0:                
                for rr in range(row):
                    printd("[%d, %d] Clear row(%d) %d to 0" % (r, c, rr, mat[rr][c]))
                    retMat[rr][c] = 0
                for cc in range(col):
                    printd("[%d, %d] Clear col(%d) %d to 0" % (r, c, cc, mat[r][cc]))
                    retMat[r][cc] = 0

    return retMat


def zeroMatrix_1st_numpyArray(mat):
    ''' Complexity: O(N^2) / O(N^2) '''
    row = len(mat)
    col = len(mat[0])

    nMat = np.array(mat)
    retMat = np.copy(nMat)

    for r in range(row):
        for c in range(col):            
            if nMat[r][c] == 0:                
                for rr in range(row):
                    printd("[%d, %d] Clear row(%d) %d to 0" % (r, c, rr, nMat[rr][c]))
                    retMat[rr][c] = 0
                for cc in range(col):
                    printd("[%d, %d] Clear col(%d) %d to 0" % (r, c, cc, nMat[r][cc]))
                    retMat[r][cc] = 0

    
    return retMat.tolist()


def zeroMatrix_1st_numpyMatrix(mat):
    ''' Complexity: O(N^2) / O(N^2) '''
    row = len(mat)
    col = len(mat[0])

    nMat = np.matrix(mat)
    retMat = np.matrix.copy(nMat)

    # Show shape and dimension
    print("Shape of matrix: ", retMat.shape)
    print("Dim of matrix: ", len(retMat.shape))
    
    # Index of row 0 in matrix
    print("Index of row 0 in matrix:", end='')
    print(nMat[0])    
    # Index of [1][1] in matrix
    print("Index of [1][1] in matrix:", end='')
    print(nMat[1,:][:,1])

    for r in range(row):
        for c in range(col):            
            if nMat[r,:][:,c] == 0:                
                for rr in range(row):
                    #printd("[%d, %d] Clear row(%d) %d to 0" % (r, c, rr, nMat[rr][c]))
                    retMat[rr,:][:,c] = 0
                for cc in range(col):
                    #printd("[%d, %d] Clear col(%d) %d to 0" % (r, c, cc, nMat[r][cc]))
                    retMat[r,:][:,cc] = 0


    printd(retMat)
    return retMat.tolist()


def zeroMatrix_2nd_list(mat):
    ''' Complexity: O(N^2) / O(c) '''
    row = len(mat)
    col = len(mat[0])

    # Set corresponding row and col to 
    zeroRow = []
    zeroCol = []
    for r in range(row):
        for c in range(col):
            if mat[r][c] == 0:
                if r not in zeroRow:
                    zeroRow.append(r)
                if c not in zeroCol:
                    zeroCol.append(c)

    for r in range(row):
        for c in range(col):
            if r in zeroRow or c in zeroCol:
                mat[r][c] = 0

    return mat


def printMatrix(mat):
    row = len(mat)
    col = len(mat[0])
    for r in range(row):
        for c in range(col):
            print(mat[r][c], end =" ")
        print("")


def main():
    mat1 = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]

    mat2 = [[1, 1, 1],
            [1, 0, 1],
            [0, 1, 1]]
 
    mat3 = [[1, 1, 1, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1]]

    matList = [mat1, mat2, mat3]

    funcList = [zeroMatrix_1st_list, zeroMatrix_1st_numpyArray, zeroMatrix_1st_numpyMatrix,
                zeroMatrix_2nd_list]

    for func in funcList:
        print(func)
        for m in matList:
            print("-------------")
            ret = func(m)
            printMatrix(ret)


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()