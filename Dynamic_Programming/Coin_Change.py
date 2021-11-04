# dynamic programming
# https://en.wikipedia.org/wiki/Dynamic_programming

# memoization
# https://en.wikipedia.org/wiki/Overlapping_subproblems

# problem
# https://www.hackerrank.com/challenges/coin-change/problem

# stackoverflow
#https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum

# coin change
n = 3 # amount to form
c = [8,3,1,2] # coins available
#p = {1,1,1},{1,2},{3} # possibilites 

#n = 4
#c = [1,2,3]
#p = {1,1,1,1},{1,1,2},{3,1},{2,2}

#n = 10
#c = [2,5,3,6]
#p = {5,5},{2,3,5},{6,2,2},{2,2,2,2,2},{3,3,2,2}



# subproblems
"""
computing previous problems again 
if n == 0 
if n > 0 and c == []
"""

'''
understanding => 
for every element i times => divide,modulus
print(i,int(n/i),n%i)

pairs or more elements => 

subset elements => 

single elements => n in c
'''
from itertools import combinations as cb

def comb(n,c):
    p = 0
    
    
    for i in range(len(c)):
        d,m = divmod(n,c[i])
        
        #twice
        if m in c and (c[i]+m)*d == n:
            p+= 1
            
        #third
        if m != 0 and c[i] <= n:
            print(c[i],d,m)
            arr = [c[i],d,m]
            for j in range(1,max(arr)+1):
                if sum(arr)+j == n or \
                sum(arr)-j == n and sum(arr) != 3:
                    p+=1
                    break
        #ones
        if m == 0 and c[i]*d+m == n:
            p+= 1
    
    #fourth and so on
    for i in range(4,len(c)+1):
        cl = list(filter
            (lambda x: sum(x) == n, 
            list(cb(c,i)))) 
        if cl != []:
            print(cl)
            p += len(cl)
    
    print(p)

comb(n,c)

#============================================================#
def pairs(arr):
    n = len(arr)
    x = [len(i) for i in arr]
    print(n,x,arr)


p = [(i,divmod(amount,i)) for i in coins if i<= amount]
print(p)

c = list(filter(lambda x: x[1][1] != 0,p))
pos = lambda x: list(range(0,x+1))
ar = [[pos(i[0]),pos(i[1][0]),pos(i[1][1])] for i in c]

for i in ar:
    pairs(i)


# l = 0
# h = 1
# arr = []

# for i in c:
#     # arr = [i[0],i[1][0],i[1][0]]
#     ar = [list(range(0,i[0])),list(range(0,i[1][0])),list(range(0,i[1][1]))]
#     h = max(arr)
#     print(arr,l,h)

#============================================================#

amount = 3 # amount to form
coins = [8,3,1,2] # coins available
#p = {1,1,1},{1,2},{3} # possibilites 

amount = 4
coins = [1,2,3]
#p = {1,1,1,1},{1,1,2},{3,1},{2,2}

# amount = 10
# coins = [2,5,3,6]
#p = {5,5},{2,3,5},{6,2,2},{2,2,2,2,2},{3,3,2,2}

p = [(i,divmod(amount,i)) for i in coins if i<= amount]

c = list(filter(lambda x: x[1][1] != 0,p))

# print(p,c)
l = 0
h = 1
arr = []
for i in c:
    arr = [i[0],i[1][0],i[1][0]]
    h = max(arr)
    print(arr,l,h)

# dp = [1] + [0]*amount

# print(amount,coins,'\n')
# for coin in coins:
#     print(coin,dp)
#     for i in range(coin, amount+1):
#         print(i,coin,i-coin,dp[i])
#         dp[i] += dp[i-coin]
#     print()

# print()
# print(dp[amount])








