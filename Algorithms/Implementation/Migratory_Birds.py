#migratory birds
# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=internal-search

from collections import Counter
arr = [1,1,2,2,3]
#arr = [1,2,2,3,3,4,5]
#arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]


"""
def migratorybirds(arr):
    d = {}
    for i in arr:
        if arr.count(i) != 1:
            d[i] = arr.count(i)
    print(d)
    f = 0 #frequency 
    n = 0 #ith value of lesser
    for i,j in d.items():
        if j > f :
            f = j
            n = i
    return n


#print(migratorybirds(arr))
"""


birds = Counter(arr)
print(birds)
print(birds.items())
print(birds.keys())
print(birds.values())
print(birds[min(birds.keys())])
#print(birds.values())