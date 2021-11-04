# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=internal-search
A = input().split()
B = input().split()


def compare(a, b):
    alice = 0
    bob = 0
    x = len(a)
    for i in range(x):
        if int(a[i]) > int(b[i]):
            alice += 1
        elif int(a[i]) < int(b[i]):
            bob += 1
        elif a[i] == b[i]:
            alice += 0
            bob += 0
        pass
    return [alice, bob]


total = compare(A, B)
print(total)

"""
Examples
17 28 30
99 16 8
output => 2, 1
5 6 7
3 6 10
output => 1, 1
"""