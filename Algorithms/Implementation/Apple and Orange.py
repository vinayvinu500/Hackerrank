#!/bin/python3
# https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=internal-search

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    point = list(range(s, t + 1))
    apple = a
    orange = b
    totalApple = []  # [sum([apple, i]) for i in apples]
    totalOrange = []  # [sum([orange, j]) for j in oranges]
    for i in apples:
        s = apple + i
        totalApple.append(s)
    for i in oranges:
        s = orange + i
        totalOrange.append(s)
    print(totalApple)
    print(totalOrange)
    for i in totalApple:
        if i in point:
            appleCount += 1
        pass
    for j in totalOrange:
        if j in point:
            orangeCount += 1
        pass
    print(appleCount)
    print(orangeCount)
    pass


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

"""
Example 
7 10
4 12
3 3
2 3 -4
3 -2 -4
output => 
1
2

7 11
5 15
3 2
-2 2 1
5 -6
output => 
1 
1
"""
