import os
# https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=internal-search

def feast(b, m, memo):
    memo += b // m
    if (b // m)*m == 0 and b // m == 0:
        return memo
    b = (b % m) + (b // m)
    return feast(b, m, memo)


n = 15
c = 3
m = 2

# print(os.listdir())
os.chdir('chocolate_feast/')
# print(os.listdir())

# test case 5
with open('test.txt', 'r+') as f:
    # retrieve txt
    test = f.readlines()
    # no. of test_case
    t = int(test.pop(0))
    # remove the line_break
    test = list(map(lambda x: x.replace('\n', ''), test))
    # split and type conversion
    test = list(map(lambda x: list(map(int, x.split())), test))

# test case 5 output
with open('output.txt', 'r+') as f:
    # retrieve txt
    output = f.readlines()
    # remove linebreak
    output = list(map(lambda x: x.replace('\n', ''), output))
    # convert str into int
    output = list(map(int, output))


test_case5 = [test[i]+[output[i]] for i in range(t)]

print(test_case5)

# total pass and fail cases
case = []

# test
for i in range(t):
    n, c, m, o = test_case5[i]
    func = feast(n//c, m, n//c)
    case.append([i, func == o])

print(case)
# failed cases
failed = list(filter(lambda x: x[1] is False, case))
print(failed)

# failed case



