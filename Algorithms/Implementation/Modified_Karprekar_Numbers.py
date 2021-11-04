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
    s = pow(n, 2)
    b = s % 10 ** e
    a = (s - b) / 10 ** e
    if sum((a, b)) == n:
        return True
    return False


def kaprekarf(x: int, p: int, b: int) -> int:
    beta = pow(x, 2) % pow(b, p)
    alpha = (pow(x, 2) - beta) // pow(b, p)
    y = alpha + beta
    return y

print(kaprekarf(5,2,25))
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

n = [5, 2, 10, 88, 105, 1, 1002]


# print([karprekar_modified(i) for i in n])
# e = [10 ** i for i in range(2, 1000)][:5]
# for i in range(len(n)):
#     print(n[i], n[i] - 10, n[i] - 100, n[i] % 10, n[i] % 100, n[i] / 10, n[i] / 100, bin(n[i]).replace('0b', ''))


def kaprekarf_cycle(x: int, p: int, b: int) -> list[int]:
    seen = []
    while x < pow(b, p) and x not in seen:
        seen.append(x)
        x = kaprekarf(x, p, b)
    if x > pow(b, p):
        return []
    cycle = []
    while x not in cycle:
        cycle.append(x)
        x = kaprekarf(x, p, b)
    return cycle
