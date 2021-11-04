# Given that 
b:float = 1.09 
g:int = 1

n = 6 # exactly 6 childrens 


p = b/100 # having of probability of success having a boy
q = 1- p # having of probability of success having not a boy
# print(p,q)


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


# P(X < 3) = P(x=1) + p(x=2)
px2 = pmf(n,1,p) + pmf(n,2,p)

# P(X >= 3) = 1 - P(X<3)
px3 = 1 - px2
print(round(px3,3))

# P(X >= 3) = P(X=3) + P(X=4) + P(X=5) + P(X=6)
px3456 = pmf(n,3,p) + pmf(n,4,p) + pmf(n,5,p) + pmf(n,6,p)
print(px3456) # wrong answer