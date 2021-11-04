import math
# https://www.hackerrank.com/challenges/grading/problem?h_r=internal-search

def gradingStudents(g, c):
    # Write your code here
    # rounded to 5
    r = []
    # final output
    re = []
    # for loop integration
    for i in g:
        if i < 37:
            r.append(i)
            pass
        else:
            mul = i / 5
            res = math.ceil(mul)
            rou = res * 5
            r.append(rou)
        pass
    print(g)
    print(r)
    for j in range(c):
        diff = abs(r[j] - g[j])
        if diff > 3:
            re.append(g[j])
        elif diff == 3:
            re.append(g[j])
        elif diff < 3:
            re.append(r[j])
            pass
        pass
    print(re)
    return re
    pass


count = int(input().strip())

grades = []
for _ in range(count):
    line = int(input().strip())
    grades.append(line)
    pass
result = gradingStudents(grades, count)
# print(result)
"""
val = 76
mul = val / 5
rou = math.ceil(mul)
# print(rou)
res = rou * 5
# print(res)

grade = [73, 67, 38, 33]

rounded = [75, 67, 40, 33 ]

for i, j in grade, rounded:
    print(i, j)
    pass
    for j in range(c):
        if g[j] == r[j]:
            res.append(g[j])
        else:
            diff = abs(r[j] - g[j])
            print(f"diff r{j} - g{j}", diff)
            if diff < 3:
                print(diff)
                res.append(r[j])
                print(res)
                pass
            pass
        pass
"""
"""
Examples
4
73
67
38
33
output =>
75, 67, 40, 33
4 
29
33
47
54
"""