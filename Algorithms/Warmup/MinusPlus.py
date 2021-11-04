# https://www.hackerrank.com/challenges/plus-minus/problem?h_r=internal-search
def plusMinus(arr, s):
    neg = 0
    pos = 0
    zer = 0
    for i in arr:
        if i <= -1:
            neg += 1
        elif i >= 1:
            pos += 1
        elif i == 0:
            zer += 1
        pass
    neg = neg / s
    neg = round(neg, 6)
    pos = pos / s
    # pos = round(pos, 6)
    zer = zer / s
    zer = round(zer, 6)
    al = [pos, neg, zer]
    index = 0
    for i in al:
        i = str(i)
        if len(i) == 3:
            # el = al.index(index)
            i = float(i)
            al[index] = format(i, '.6f')
        index += 1
        pass
    return al
    pass


n = int(input())

# arr = list(map(int, input().rstrip().split()))
a = input().split()

ar = []
for y in a:
    ar.append(int(y))
    pass

res = plusMinus(ar, n)
for x in res:
    print(x)
    pass
