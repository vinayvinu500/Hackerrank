# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=internal-search
# array = [1, 3, 2, 6, 1, 2]
# array = [1, 2, 3, 4, 5, 6]
# array = [1,2]
array = [0, 4, 2, 1, 0, 1]
val = 1
size = len(array)

# testing
# if k = 1 then arr = [0,1]


def divisibleSumPairs(n, k, ar):
    dsp = [(i, j) for i in ar for j in ar if i < j and k % 2 == 0 and (i + j) % k == 0]
    print(dsp, len(dsp))


divisibleSumPairs(size, val, array)
