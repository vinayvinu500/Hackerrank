# https://www.hackerrank.com/challenges/red-john-is-back/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

from math import factorial as fc
from itertools import permutations as pt

def comb(n,r):
    return fc(n)/(fc(n-r)*fc(r))

def prime(n):
    if n == 0 or n == 1: return False 
    if n == 2: return True
    i = 2
    while i <= n/2:
        if n%i == 0:
            return False
        i+=1
    return True


# understanding
"""
block of wall which is either 1xn or nx1
prime numbers in range of 0,n (inclusive)
"""

n = [1,3,5,7]

# block of wall
# matrix_one = (1,n)
# matrix_two = (n,1)

# wall size nx4


for x in n:
    s = 4
    w = list(range(s))
    wall = list(pt(w,4))
    print(wall)


# for x in n:
#     m_row = (1,[i for i in range(0,x)])
#     m_col = ([i for i in range(0,x)],1)
#     m_rc = m_row+m_col
#     print(m_row)
#     print(m_col)
#     print(m_rc)
#     print()


# for i in n:
#     w = list(range(0,i))
#     ar = list(pt(w,))
#     p = list(map(prime,w))
#     print(ar)
#     print(i,p,p.count(True))
#     print()