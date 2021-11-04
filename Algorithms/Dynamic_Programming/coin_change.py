# https://www.hackerrank.com/challenges/reduced-string/problem?h_r=internal-search
# imports
from itertools import combinations as cb
from math import factorial as fact

# dynamic programming
# https://en.wikipedia.org/wiki/Dynamic_programming

# memoization
# https://en.wikipedia.org/wiki/Overlapping_subproblems

# problem
# https://www.hackerrank.com/challenges/coin-change/problem

# stackoverflow
# https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum

# coin change
n = 3  # amount to form
c = [8, 3, 1, 2]  # coins available
# p = {1,1,1},{1,2},{3} # possibilities

# n = 4
# c = [1,2,3]
# p = {1,1,1,1},{1,1,2},{3,1},{2,2}

# n = 10
# c = [2,5,3,6]
# p = {5,5},{2,3,5},{6,2,2},{2,2,2,2,2},{3,3,2,2}


bc = lambda n,x: fact(n)/(fact(x)*fact(n-x))
possibilities = [(i,bc(n,i)) for i in c if i <= n]
print(possibilities)

print(n,c)
for i in c:
    print(i,divmod(n,i))


# binomial distribution
def binomial(n, x, p):
    return (fact(n)/(fact(x)*fact(n-x))) * p ** x * (1-p) ** (n-x)




# sub_problems
"""
computing previous problems again 
if n == 0 
if n > 0 and c == []
"""

'''
understanding => 
for every element i times => divide,modulus
print('divmod(n,i) => ',i,int(n/i),n%i)

pairs or more elements => 

subset elements => 

single elements => n in c
'''


def comb(n, c):
    p = 0

    for i in range(len(c)):
        d, m = divmod(n, c[i])

        # twice
        if m in c and (c[i] + m) * d == n:
            p += 1

        # third
        if m != 0 and c[i] <= n:
            print(c[i], d, m)
            arr = [c[i], d, m]
            for j in range(1, max(arr) + 1):
                if sum(arr) + j == n or \
                        sum(arr) - j == n and sum(arr) != 3:
                    p += 1
                    break
        # ones
        if m == 0 and c[i] * d + m == n:
            p += 1

    # fourth and so on
    for i in range(4, len(c) + 1):
        cl = list(filter
                  (lambda x: sum(x) == n,
                   list(cb(c, i))))
        if cl != []:
            print(cl)
            p += len(cl)

    print(p)

# comb(n, c)
