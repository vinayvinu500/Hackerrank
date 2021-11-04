import string
# https://www.hackerrank.com/challenges/gem-stones/problem?h_r=internal-search
# ascii_lowercase -> 95-123

import string

l = string.ascii_lowercase

ind = l.index('a')

ar = [0 for _ in range(len(l))]

arr = ['abcdde', 'baccd', 'eeabg']

arr = [set(i) for i in arr]

print(len(arr),arr)

for i in arr:
    for j in i:
        ind = l.index(j)
        ar[ind] += 1

print(ar)

print(ar.count(len(arr)))

# https://www.hackerrank.com/challenges/gem-stones/problem
# Dynamic problem
import string


arr = ['abcdde', 'baccd', 'eeabg']
l = string.ascii_lowercase
alpha = [[0]*len(l) for _ in range(len(l))]

# representation
print(' ',' '.join(l))
for o1,i in enumerate(alpha):
    print(l[o1],end=' ')
    for j in i:
        print(j,end=' ')
    print()

# procedure
print()
print(arr)


#=====================================================#
# d = {}
# for i in range(len(l)):
#     d[l[i]] = i
# alpha = [0]*len(l)

# gem = ['abc','abc','bc']
# gem = ['abcdde', 'baccd', 'eeabg']

# for i in gem:
#     for j in i:
#         # print(i,j)
#         alpha[d[j]] += 1

# print(alpha)
# m = alpha.count(max(alpha))
# print(m)

#=====================================================#
