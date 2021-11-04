l = 1
u = 1000000

# https://www.hackerrank.com/challenges/kaprekar-numbers/problem?h_r=internal-search
# https://en.wikipedia.org/wiki/Kaprekar_number
# https://betterexplained.com/articles/numbers-and-bases/


# method 1 -> square -> str -> split -> sum
def karprekar(n):
    if n == 1:
        return True
    if n in (2, 3):
        return False
    s = str(n ** 2)
    l = len(s)
    m = l // 2
    ar = [s[:m], s[m:]]
    ar = list(map(int, ar))
    if sum(ar) == n:
        return True
    return False


# method 2
def karprekar_modified(n):
    e = len(str(n))
    s = n ** 2
    b = s % 10 ** e
    a = (s - b) / 10 ** e
    if sum((a, b)) == n:
        return True
    return False


#
# # arr1 = []
# arr2 = []
# n = 100000
# for i in range(1, n+1):
#     # if karprekar(i):
#     #     arr1.append(i)
#     if karprekar_modified(i):
#         arr2.append(i)
#
# # print(arr1)
# print(arr2)

e = [10 ** i for i in range(1, 100)][:5]
for i in range(1, 100, 10):
    print(i - 10)
