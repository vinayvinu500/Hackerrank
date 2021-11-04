# user input
# https://www.hackerrank.com/challenges/staircase/problem?h_r=internal-search
n = int(input())

# build a staircase of base and height are equal to n
spaces = ' '
hashes = '#'
# print(spaces * (n-1))
# for loop integration
count = 1
for i in range(n):
    s = spaces * (n-count)  # spaces will decrease by n
    h = hashes * count  # hashes will increase by n
    print(s+h)
    count += 1
    pass
