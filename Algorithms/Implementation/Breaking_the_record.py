# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=internal-search
def breakingRecords(scores):
    l, h = scores[0], scores[0]
    b, w = 0, 0
    lowest = []
    highest = []
    for i in scores:
        if i > h:
            h = i
            b += 1
        if i < l:
            l = i
            w += 1
        highest.append(h)
        lowest.append(l)
        # print(i, l, h, lowest, highest)
    print('scores = \t', scores)
    print('highest = ', highest)
    print('lowest = \t', lowest)
    return b, w


arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
# arr = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(arr))
