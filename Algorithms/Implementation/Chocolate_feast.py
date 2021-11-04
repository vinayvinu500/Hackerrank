# chocolate feast
# https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=internal-search

n = 15 #money
c = 3 #price
m = 2 #discount
"""
n = 15 rupees in hand
c =  3 each chocolate
m = 2 wrappers exchange by 1

inital => [1,1,1,1,1] # exchange 15rs by 3 = 5
first => [1,1,1,1,1] # exchange 4 by 2
second => [1,1,1] # exchange 2 by 1
third => [1,1] # exchange 2 by 1
last => [1]

total => 5 + 2 + 1 + 1 => 9
"""
#trail 1
n = 10
c = 2
m = 5

#trail 2
n = 12
c = 4
m = 4
"""
n = 12 rupees in hand
c =  4 each chocolate
m = 4 wrappers exchange by 1

# exchange 12rs by 4 = 3
inital => [1,1,1] # exchange not posible 

total => 3
"""

#trail 3
n = 6
c = 2
m = 2

#trail 4
# n = 43203
# c = 60
# m = 5


print('rupees = ',n,'\nprice = ',c)
# recursive function
def feast(b,m,memo):
    memo += b//m
    print('chocolates = ',b,'\navailable = ',memo,'\ngiven = ',(b//m)*m,'\nreturned  = ',(b//m),'\nremaining  = ',(b%m),'\n')
    if (b//m)*m == 0 and b//m == 0:
        return memo
    b = (b//m) + (b%m)
    return feast(b,m,memo)
    


print(feast(n//c,m,n//c))