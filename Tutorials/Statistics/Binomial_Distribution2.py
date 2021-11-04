#https://www.geeksforgeeks.org/python-binomial-distribution/
#https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial

import sys
import scipy.stats
import matplotlib.pyplot as plt


def fact(x,memo={}):
    # factorial of x! = x * (x-1) * (x-2) * ..... 2 * 1
    if x in memo:
        return memo[x]
    if x <= 1:
        return 1
    memo[x] = x*fact(x-1,memo)
    return memo[x]
    
def bin_coe(n,x):
    # binomial coefficient = n! / x!(n-x)!
    return fact(n) / (fact(x) * fact(n-x))

def pmf(n,x,p):
    # probability mass function for the binomial distribution
    return bin_coe(n,x) * (p**x) * ((1-p)**(n-x))

n = 10
x = list(range(1,11))
p = 0.5
q = 0.5

# mean = np; variance = np(1-p)
mean, variance = scipy.stats.binom.stats(n, p)

print(mean, variance)

# p(x) = nCr (p^x) ((1-p)^n-r)
px = [scipy.stats.binom.pmf(r, n, p) for r in x]

print(x)
print(px)

plt.bar(x, px)

plt.title('A coin is tossed 10 times')
plt.xlabel("The value of X")
plt.ylabel("Probability of x")


# plt.hist(px)
plt.show()
plt.savefig('binomial.png')

#Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# print(px[4])
# print(sum(px[4:]))
# print(sum(px[:5]))