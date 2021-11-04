#modified fibonacci
# https://www.hackerrank.com/challenges/fibonacci-modified/problem?h_r=internal-search

#formula ti+2 = ti + (ti+1)^2

t1 = 0
t2 = 1
n = 6


def fib(t1,t2,n):
    memo=[t1,t2]
    for i in range(2,n):
        print(i,memo)
        memo.append(memo[-2]+memo[-1]**2)
    print(memo)
    return memo[-1]

print(fib(t1,t2,n))