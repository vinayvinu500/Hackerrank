# https://www.hackerrank.com/challenges/weighted-uniform-string/problem?h_r=internal-search

import string
from collections import Counter

l = string.ascii_lowercase
s = 'abccddde'
d = {}
for i,j in enumerate(l,1):
    d[j] = i
e = Counter(s)
w_c = []
w = []
for i,j in e.items():
    for k in range(1,j+1):
        w_c.append(i*k)
        w.append(d[i]*k)

print(d)
print(l)
print(s)
print(e)
print(w)
print(w_c)

q = [1, 3, 12, 5, 9, 10]
for i in q:
    if i in w:
        print('Yes')
    else:
        print('No')