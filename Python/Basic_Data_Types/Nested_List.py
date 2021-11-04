# user input
# https://www.hackerrank.com/challenges/nested-list/problem?h_r=internal-search
if __name__ == '__main__':
    z = int(input())
    phy = []
    grd = []
    for _ in range(z):
        name = input().strip()
        score = float(input().strip())
        phy.append([name, score])
        grd.append(score)
        pass
    phy.sort()
    grd.sort()
    sco = grd[1]
    cou = grd.count(sco)
    if cou == 1:
        for i in range(len(phy)):
            if sco == phy[i][1]:
                key, val = phy[i]
                output = [key]
                print(output[0])
        pass
    else:
        for i in range(len(phy)):
            if sco == phy[i][1]:
                key, val = phy[i]
                output = [key]
                output.sort()
                for j in output:
                    print(j)
            pass
        pass

    """
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

    """
"""
arr = []
sc = []

# method 2
z = int(input())
arr = [[input().strip(), float(input())] for _ in range(z)]
print(arr)
"""
"""
# method 1
# for loop integration
z = int(input())
for i in range(z):
    name = input().strip()
    score = input().strip()
    arr.append([name, score])
    sc.append(score)
    pass

x = 1
y = 0
mi = min(sc)
co = sc.count(mi)
# if first least is more
if co > 1:
    for i in range(co):
        sc.remove(mi)
    pass
elif co == 1:
    sc.remove(mi)
# if second least is more
mi = min(sc)
co = sc.count(mi)
# if count is more than 1
if co > 1:
    output = []
    for i in range(z):
        val, key = arr[i][x], arr[i][y]
        if val == mi:
            output.append(key)
        pass
    output.sort()
    for i in output:
        print(i)
    pass
# if count is equal to 1
elif co == 1:
    output = []
    for i in range(z):
        val,key = arr[i][x],arr[i][y]
        if val == mi:
            output.append(key)
        pass
    output.sort()
    for i in output:
        print(i)
    pass
"""
"""
Examples
5 
Harry 
37.2 
Berry 
37.21 
Tina 
37.2 
Akriti 
41 
Harsh 
39
"""