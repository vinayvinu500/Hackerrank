# sequence equation
# https://www.hackerrank.com/challenges/permutation-equation/problem?h_r=internal-search


arr = [5,2,1,3,4] # array
arr = [2,3,1]
#arr = [4,3,5,1,2]
ind = [i for i in range(1,len(arr)+1)] # indices
# val,ind = x,p[x]
a = sorted([(j,i) for i,j in enumerate(arr,1)]) # val,ind
b = [i[1] for i in a] # p[x]
c = [b[i-1] for i in b] # p[x] = x

print(arr)
print(ind)
print(a)
print(b)
print(c)
