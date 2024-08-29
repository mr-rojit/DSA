"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

EG

Input:
matrix = 
        [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

Output:[
        [7,4,1],
        [8,5,2],
        [9,6,3]
]

Eg 2:

Input: matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
Output: [
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    16,7,10,11]
]

"""

def rotate_matrix(mat):

    n = len(mat) - 1

    f,l = 0, n

    while f<l:
        temp = mat[f]
        mat[f] = mat[l]
        mat[l] = temp

        f+=1
        l-=1

    for i in range(n+1):
        for j in range(i,n+1):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp


M = [[5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]]

rotate_matrix(M)

print(M)