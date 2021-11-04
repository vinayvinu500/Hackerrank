# https://www.hackerrank.com/challenges/icecream-parlor/problem?h_r=internal-search

# algorithm => index-base 
def pool(cost,money):
    # length
    n = len(cost)

    # loop execution
    for i in range(n//2):
        # indices
        f = i
        b = (n-1)-i
        m = n//2

        # directions
        front = abs(money-cost[f])
        if front in cost and front != cost[f]:
            x = f,cost[f]
            y = cost.index(front),front
            break
        elif cost.count(front) == 2:
            x = f,cost[f]
            y = cost.index(front,f+1),front
            break
        midlef = abs(money-cost[m-i])
        if midlef in cost and midlef != cost[m-i]:
            x = m-i,cost[m-i]
            y = cost.index(midlef),midlef
            break
        midrig = abs(money-cost[m+i])
        if midrig in cost and midrig != cost[m+i]:
            x = m+i,cost[m+i]
            y = cost.index(midrig),midrig
            break
        back = abs(money-cost[b])
        if back in cost and back != cost[b]:
            x = b,cost[b]
            y = cost.index(back),back
            break
            
    # representation            
    fav = (x[0],y[0]),(x[1],y[1])
    ar = [x[0]+1,y[0]+1]
    print(min(ar),max(ar))
    return ' '.join((str(min(ar)),str(max(ar))))


# example 
cost = [2, 1, 3, 5, 6]
money = 5

cost = [1, 4, 5, 3, 2]
money = 4

cost = [2, 2, 4, 3]
money = 4

cost = [1, 2, 3, 5, 6]
money = 5

cost = [4, 3, 2, 5, 7]
money = 8

cost = [7, 2, 5, 4, 11]
money = 12

# money, cost, result
t = [(8,[4, 3, 2, 5, 7],(2, 4)),(12,[7, 2, 5, 4, 11],(1, 3)),(4,[1, 4, 5, 3, 2],(1, 4)),(4,[2, 2, 4, 3],(1, 2))]

for o in t:
    money,cost,ind = o
    pool(cost,money)

# sample test case
# money,cost,ind = t[-1]    
# pool(cost,money)