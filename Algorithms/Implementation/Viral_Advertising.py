# https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=internal-search

shared = [5]
liked = [2]
cummulative = [2]

for i in range(2,6):
    shared.append(liked[-1]*3)
    liked.append(shared[-1]//2)
    cummulative.append(liked[-1]+cummulative[-1])
    

for i in range(5):
    print(i+1,shared[i],liked[i],cummulative[i])

print(cummulative[5-1])