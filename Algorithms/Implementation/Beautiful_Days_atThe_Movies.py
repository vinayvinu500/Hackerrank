#beautiful day
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=internal-search

def swap(n):
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    return rev

def bd(i,j,k):
    arr = [(abs(i-swap(i)))/k for i in range(i,j+1)]
    temp  = list(map(lambda x: x==int(x),arr))
    print(arr)
    print(temp)
    return temp.count(True)
    
print(bd(20,23,6))

a = 2
b = 2.5
print(isinstance(a,int))
print(isinstance(a,float))