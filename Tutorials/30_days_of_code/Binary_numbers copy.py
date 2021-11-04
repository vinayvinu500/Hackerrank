#base 3 to base 10
#number = 21 base 3
#number = 2(3^1) + 1(3^0) 
#number = 7 base 10
# https://www.hackerrank.com/challenges/30-binary-numbers/problem?h_r=internal-search


def base10(n):
    l = len(n) 
    if b == 10:
        return int(n)
    else:
        b10 = [int(n[i]) * b **(l-i-1) for i in range(l)]
        return sum(b10)

number = '0111'
k = 2
b = 10
m = 100
le = len(number)
n = [number[i:k+i] for i in range(le) if len(number[i:k+i]) == k]
b10 = list(map(base10,n))
mod = list(map(lambda x: x%m,b10))
magic_num = sum(mod)

#result
print('n = ',n)
print('b10 = ',b10)
print('mod = ',mod)
print(magic_num)
"""
def convert(num):
    if num <= 1:
        return 1
    else:
       return (num % 2 + 10 * convert(num // 2))
   
print(convert(int(input())))
"""