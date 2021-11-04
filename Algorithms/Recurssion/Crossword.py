# https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_r=internal-search
####################################################
st = []
# structure
for _ in range(10):
    line = input()
    st.append(line)
    pass
for _ in range(len(st)):
    print(st[_])
    pass
len_st = []
for m in range(len(st)):
    l = st[m].count('-')
    len_st.append(l)
    pass
# print(len_st)


####################################################
wo = input("words: ").split(';')
a, b, c, d = wo
len_a = len(a)
len_b = len(b)
len_c = len(c)
len_d = len(d)
len_wo = [len_a, len_b, len_c, len_d]
# words to fit
first = set()
for _ in range(2):
    for i in a:
        for j in b:
            if i is j:
                first.add(i)
            pass

print(first)
second = set()
for _ in range(2):
    for x in c:
        for y in d:
            if x is y:
                second.add(x)
            pass
print(second)

###############################################
''' Condition'''
words = set()
for i in len_st:
    for j in wo:
        if i is len(j):
            words.add(j)
        pass
print(words)
###############################################
'''
Examples
XXXXXX-XXX
XX------XX
XXXXXX-XXX
XXXXXX-XXX
XXX------X
XXXXXX-X-X
XXXXXX-X-X
XXXXXXXX-X
XXXXXXXX-X
XXXXXXXX-X
ICELAND;MEXICO;PANAMA;ALMATY
'''
