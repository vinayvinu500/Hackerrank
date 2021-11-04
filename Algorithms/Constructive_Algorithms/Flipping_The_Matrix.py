# flipping a matrix
# https://www.hackerrank.com/challenges/flipping-the-matrix/problem?h_r=internal-search

# pattern
'''
row 
col

flip a matrix 
Row => 0r
Col => 1c

matrix => 2n x 2n 
where original matrix is n x n

Task : max sum of nxn matrix

replaced terms of size of n = 4 => 4x4 matrix
m[0][0] => m[0][-1],m[-1][0],m[-1][-1]
m[1][0] => m[1][-1],m[2][0],m[2][-1]
m[0][1] => m[-1][1],m[0][-2],m[-1][-2]
m[1][1] => m[1][-2],m[2][1],m[2][2]
'''
matrix = [
    [1,2],
    [3,4]
]

matrix = [
    [112,42,83,119],
    [56,125,56,49],
    [15,78,101,43],
    [62,98,114,108]
]

# flipping matrix by r = row, c = col
def flip(k,m):
    x,s = int(k[0]),k[1]
    n = len(m[0])
    
    if s == 'r':
        for i in range(n//2):
            m[x][i],m[x][n-1-i] = m[x][n-1-i],m[x][i]
    if s == 'c':
        for i in range(n//2):
            m[i][x],m[n-1-i][x] = m[n-1-i][x],m[i][x]
            

# representation of matrix
def repr(m):
    n = len(m[0])
    for i in range(n):
        for j in range(n):
            print(m[i][j],end=' ')
        print()
    print()


# logic for the matrix
def flippingMatrix(m):
    n = len(m[0])
    
    
    repr(m)
    flip('0r',m)
    repr(m)
    flip('0c',m)
    repr(m)

flippingMatrix(matrix)







