# https://www.hackerrank.com/challenges/s10-mcq-1/problem
"""
d = list(range(1,7))

pt = [(i,j) for i in d for j in d]

outof9 = []
c = 0
for i in range(len(pt)):
    if i in range(6,len(pt),6):
        print()
    if sum(pt[i]) <= 9: # at most 9
        c += 1
    else:
        outof9.append(pt[i])
    print(pt[i],sum(pt[i]),end=' ')
    
print()
print(c)
print(outof9)

from fractions import Fraction
p = Fraction(c, len(pt)) 
# fav outcomes / total outcomes

print(p)

# https://www.hackerrank.com/challenges/s10-mcq-2/problem
#from itertools import combinations as cb,permutations as pt

#dice = list(pt([1,2,3,4,5,6],2))
print()
sum_6 = []
for i in pt:
    if sum(i) == 6 and i[0] != i[1]:
        sum_6.append(i)
print(pt,len(pt))
print(sum_6,len(sum_6))
print(Fraction(len(sum_6),len(pt)))
"""

# coursera
from itertools import combinations as cb, permutations as pt
coin = ['H','T'] * 5 # tossed 5 times
sample = list(cb(coin,4)) # at most 4 tails
tails4 = list(filter(lambda x: 'T' in x,sample))

s = len(sample)
t = len(tails4)

print(t/s)