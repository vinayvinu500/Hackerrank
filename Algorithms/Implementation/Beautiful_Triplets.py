# beautiful triples
# https://www.hackerrank.com/challenges/beautiful-triplets/problem?h_r=internal-search

#from itertools import permutations as pt, combinations as cb
#print(list(cb(range(10**4),3)))

arr = [2,2,3,4,5]
d = 1

arr =[1,2,4,5,7,8,10]
d = 3

####################################################
n = len(arr)

t = 0
# i < j < k
# j - i = k - j = d

print(arr)
print()
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(i+2,n):
            if arr[i] < arr[j] < arr[k] and arr[j]-arr[i] == arr[k]-arr[j] == d:    
                print(arr[i],arr[j],arr[k])
                t += 1

print()
print(t)