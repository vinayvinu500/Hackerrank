# https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product as pd

k, m = [3, 1000]
ki = [2,3,5]
v = [[5,4],[7,8,9],[5,7,8,9,10],[1,2,3,4,5,6,7],[346,345,524,464,2445,2345],[753,2034798,14364273,10234987,443578,3408714],[1023478,4359,13983,23870934,34084,1239823,14287]]

n = list(pd(*v))

it = []

for i in n:
    a = sum(list(map(lambda x: x**2,i)))%m
    it.append(a)
    # print(i,a)

print(it)
print(max(it))

'''
Understood
from itertools import combinations as cb, product as pd
import numpy as np

# https://www.hackerrank.com/challenges/maximize-it/problem
# https://en.wikipedia.org/wiki/Perfect_number

'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

# sample 2
7 867
7 6429964 4173738 9941618 2744666 5392018 5813128 9452095
7 6517823 4135421 6418713 9924958 9370532 7940650 2027017
7 1506500 3460933 1550284 3679489 4538773 5216621 5645660
7 7443563 5181142 8804416 8726696 5358847 7155276 4433125
7 2230555 3920370 7851992 1176871 610460 309961 3921536
7 8518829 8639441 3373630 5036651 5291213 2308694 7477960
7 7178097 249343 9504976 8684596 6226627 1055259 4880436
'''
# k, m = list(map(int, input().split()))
# el, n = [], []
#
# for i in range(k):
#     i = list(map(int, input().split()))
#     n.append(i[0])
#     el.append((i[1:]))
#
# print(el)
# m = max(n)
# ar = [el[i]+[0]*abs(len(el[i])-m) for i in range(k)]
# print(ar)

# c = list(pd(*el))
# print(c)

# smax = [sum(list(map(lambda x: x**x, i))) % m for i in c]
# print(smax)

# k,m = 7, 867 el = [[6429964, 4173738, 9941618, 2744666, 5392018, 5813128, 9452095], [6517823, 4135421, 6418713,
# 9924958, 9370532, 7940650, 2027017], [1506500, 3460933, 1550284, 3679489, 4538773, 5216621, 5645660], [7443563,
# 5181142, 8804416, 8726696, 5358847, 7155276, 4433125], [2230555, 3920370, 7851992, 1176871, 610460, 309961,
# 3921536], [8518829, 8639441, 3373630, 5036651, 5291213, 2308694, 7477960], [7178097, 249343, 9504976, 8684596,
# 6226627, 1055259, 4880436]]

k, m = 3, 1000
n = [2, 3, 5]
el = [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]


def mean(arr):
    return sum(arr) / len(arr)


def std(arr):
    m = mean(arr)
    return sum([(i-m)**2 for i in arr])


x = [mean(i) for i in el]
s = [std(i) for i in el]
print(x)
print(s)
print()

for i in n:
    for j in range(i):
        print()
    print()

'''