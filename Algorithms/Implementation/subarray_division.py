# https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=internal-search
def birthday(s, d, m):
    sub = [s[i:m+i] for i, j in enumerate(s)]
    arr = list(map(lambda x: sum(x) == d, sub))
    print(s)
    print(sub)
    print(arr)
    return arr.count(True)


array = [4]
day = 4
month = 1
print(birthday(array, day, month))
