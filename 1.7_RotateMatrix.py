#--------------------------------------------------
# Rotate matrix for 90 degree
#--------------------------------------------------
'''
Todo:
  1. Implement in-place rotate matrix
  
Hint:
  1. Rotate by layer
  2. Rotate 4 layers at same time

Note:

'''

import numpy as np
import math

DEBUG = 0
def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def rotateMatrix_1st(mat):
    ''' Use copy to rotate matrix, complexity: O(N^2) / O(N^2) '''
    row = len(mat)
    col = len(mat[0])

    # Directly return original matrix if not NxN matrix
    if row != col:
        return mat

    # NxN matrix
    n = row

    # Declaire new 2d array based on original 2d array
    retMatClock = [[0 for c in range(col)] for r in range(row)]
    retMatCounterClock = [[0 for c in range(col)] for r in range(row)]

    # Copy 2d array
    for r in range(row):
        for c in range(col):
            # Clockwise
            printd("+Pos(%d,%d) to (%d,%d): %d" % (r, c, c, n-1-r, mat[r][c]))
            retMatClock[c][n - 1 - r] = mat[r][c]
            
            # Counter clockwise
            printd("-Pos(%d,%d) to (%d,%d): %d" % (r, c, c, n-1-r, mat[r][n-1-r]))
            retMatCounterClock[r][c] = mat[c][n - 1 - r]

    return retMatClock, retMatCounterClock


def rotateMatrix_2nd(mat):
    ''' In-place rotate matrix, complexity: O(N^2) / O(N^2) '''
    row = len(mat)
    col = len(mat[0])

    # Directly return original matrix if not NxN matrix
    if row != col:
        return mat

    # NxN matrix
    n = row

    nLayers = math.ceil(n/2)

    for l in range(nLayers):
        width = n - l*2 - 1
        printd("Layers(%d/%d) width(%d)" % (l, nLayers, width))
        for w in range(0, width):
            printd(" T (%d,%d)=%2d, R (%d,%d)=%2d, B (%d,%d)=%2d, L (%d,%d)=%2d"%
                       (l, l+w, mat[l][l+w],
                        l+w, l+width, mat[l+w][l+width],
                        l+width, n-(l+w+1), mat[l+width][n-(l+w+1)],
                        n-(l+w+1), l, mat[n-(l+w+1)][l] ))
            
            # Left
            tmp = mat[n-(l+w+1)][l]
            # Left = Bottom
            mat[n-(l+w+1)][l] = mat[l+width][n-(l+w+1)]
            # Bottom = Right  
            mat[l+width][n-(l+w+1)] = mat[l+w][l+width]
            # Right = Top
            mat[l+w][l+width] = mat[l][l+w]
            # Top = original Left
            mat[l][l+w] = tmp 
            

    return mat, mat


def printMatrix(mat):
    row = len(mat)
    col = len(mat[0])
    for r in range(row):
        for c in range(col):
            print("%2d " % mat[r][c], end =" ")
        print("")


def main():
    mat1 = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]

    mat2 = [[0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]]

    mat3 = np.arange(25).reshape((5, 5))

    matList = [mat1, mat2, mat3]

    funcList = [rotateMatrix_1st, rotateMatrix_2nd]

    for func in funcList:
        print(func)
        for m in matList:
            print("===============")
            printMatrix(m)
            
            ret1, ret2 = func(m)
            print("---------------")
            printMatrix(ret1)
            print("---------------")
            printMatrix(ret2)            


#####################
#  File entry point
#####################
if __name__=='__main__':
    main()