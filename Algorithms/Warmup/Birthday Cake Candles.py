# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=internal-search
def birthdayCakeCandles(arr, s):
    counter = 0
    m = max(arr)
    c = arr.count(m)
    if c > 1:
        counter = c
    return counter
    pass


size = int(input())
a = input().split()
ar = []
for j in a:
    ar.append(int(j))
    pass
# print(ar)
res = birthdayCakeCandles(ar, size)
print(res)

"""
# method 2
counter = 0
    for i in range(s):
        m = max(arr)
        c = arr.count(m)
        print(c)
        if c > 1:
            # arr.remove(m)
            counter += 1
            pass
        # arr.remove(m)
        pass
    return counter
"""