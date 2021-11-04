# Dancing in pairs
# https://www.hackerrank.com/challenges/dance-class/problem


def pairs(n,e=10):
    x = lambda: s.append('x')
    o = lambda: s.append('o')
    attend = (x,o)

    arr = range(e+n) # indexing
    s = [] # student
    a = 0 # attending 

    for i in arr:
        if i in arr[n-1:e+1+n:n]:
            a = 1 if a == 0 else 0
        attend[a]()

    return s

def solve(i):
    if i == 1:
        return 'odd'
    # students attends
    days = [pairs(x) for x in range(1,i+1)] # days of students
    # N(i) = day
    day = [days[x][i-1] for x in range(len(days))]
    c = day.count('o') 
    
    print('length = ',i)
    for a in days:
        print(a)
    print(day)
    
    if c%2 == 0:
        return 'even'
    return 'odd'
    
for i in range(1,5):
    #print(pairs(i))
    #print(solve(i))
    pass
print(pairs(12))