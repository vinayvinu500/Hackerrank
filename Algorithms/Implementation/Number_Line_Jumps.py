
#kangaroo
"""
v = d / t
but time is not important jumps are calculated
v = d / j
d = vj
x1,v1 => kang1(pos),kang1(speed)
x1,v1 => kang2(pos),kang2(speed)

formula 
x1 + v1j = x2 + v2j
v1j - v2j = x2 - x1
j(v1 - v2) = x2 - x1
j = (x2-x1) / (v1-v2)
if j is int value not float value then the position of two kangaroo meet at the location is same after same jumps
Note: v1 should be greater than v2 and v1 should not be same as v2
"""


x1, v1 = 0,4
x2, v2 = 2,2

j = (x2 - x1) % (v1-v2)

print(j)
"""
d = 50
print('distance d1= ',d*v1)
print('distance d2= ',d*v2)

kangaroo1 = [i for i in range(k1, d*v1, v1)]
kangaroo2 = [i for i in range(k2, d*v2, v2)]

print(kangaroo1) #locations of kangaroo1 
print(kangaroo2) #locations of kangaroo2 

kangaroo1.pop(0)
kangaroo2.pop(0)

loc = tuple(filter(lambda x: x in kangaroo2 and kangaroo2.index(x) == kangaroo1.index(x),kangaroo1))

print(loc) # same location at the same time

match = 'YES' if len(loc) !=0 else 'NO'

print(match)
"""
"""
for i in range(d):
    if kangaroo1[i] == kangaroo2[i]:
        print(i)
        break
for i,j in enumerate(zip(kangaroo1,kangaroo2)):
    if j[0] == j[1]:
        print(i)

"""

'''
#numpy edition
import numpy as np
kang1 = np.arange(k1,d,v1)
kang2 = np.arange(k2,d,v2)

print(kang1)
print(kang2)

#indexing of element
sloc = tuple(filter(lambda x: x in kang2 and  kang1.tolist().index(x) == kang2.tolist().index(x),kang1))
#print(sloc)

match = 'YES' if len(sloc) !=0 else 'NO'

print(match)

#trying and experiment on numpy indexing
#print(np.where(kang1==12),np.where(kang2==12))
#kloc = tuple(filter(lambda x: np.where(kang1==x)==np.where(kang2==x),kang1))
#for i in kang1:
#    if np.where(kang1==i)==np.where(kang2==i):
#        print(i)
#location = kang1.tolist().index(12)
#print(location)
'''

'''
# https://www.hackerrank.com/challenges/kangaroo/problem?h_r=internal-search
def kangaroo(x1, v1, x2, v2):
    # summation
    k1 = x1 + v1
    k2 = x2 + v2
    # meet
    s1 = 0
    s2 = 0
    S1 = []
    S2 = []
    for i in range(x1, 11):
        s1 += v1
        S1.append(s1)
    for i in range(x2, 11):
        s2 += v2
        S2.append(s2)
    print(S1)
    print(S2)
    # for loop integration
    y = 0
    for i in S1:
        for j in S2:
            if i == j:
                y += 1
                break
        pass
    print(y)
    print(x1 + y * v1)
    print(x2 + y * v2)
    print((x1 - x2) % (v1 - v2))
    # if k1 != k2 and meet != 'YES':
    #     return 'NO'
    # elif k1 == k2 and meet == 'YES':
    #     return 'YES'
    pass


x1V1X2V2 = input().split()

X1 = int(x1V1X2V2[0])

V1 = int(x1V1X2V2[1])

X2 = int(x1V1X2V2[2])

V2 = int(x1V1X2V2[3])

res = kangaroo(X1, V1, X2, V2)

print(res)

'''
Example
0 2 5 3
NO
0 3 4 2
YES
'''

'''