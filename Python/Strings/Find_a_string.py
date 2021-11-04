import re
# https://www.hackerrank.com/challenges/find-a-string/problem?h_r=internal-search

def count_substring(string, sub_string):
    pattern = re.compile(sub_string)
    match = pattern.search(string)
    print(match)
    count = 0
    # while loop integration
    while match is not None:
        count += 1
        a, b = match.span()
        if string[b-1:len(string)] in sub_string:
            break
        pattern = re.compile(sub_string)
        match = pattern.search(string[b-1:len(string)])
        print(string[b - 1:len(string)])
        print(match)
        pass
    return count


st = input().strip()
su = input().strip()
res = count_substring(st, su)
print(res)

# method 1
'''
if match is None:
    print(count)
else:
    count += 1
    a, b = match.span()
    pattern = re.compile(sub_string)
    match = pattern.search(string[a:len(string)])
    print(match)
    if match is None:
        print(count)
    else:
        count += 1
        print(count)
'''

'''
# method 2
st = ','.join(string)
su = ','.join(sub_string)

print(st)
print(su)

s = ''
for i in string:
    for j in sub_string:
        if j == i:
            s += i
    pass

print(s)
'''
