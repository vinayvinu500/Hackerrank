# https://www.hackerrank.com/challenges/strange-code/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
starting = 3
index = 1

# time and value seperated by 2 min
time,value = [],[]
for i in range(1,40+1):
    time.append(index) # time
    value.append(starting) # value
    index = starting+index
    starting *= 2

cycle = list(zip(time,value))

# time
t = 213921847123

# value to find in time
f = 0
for i in range(len(time)):
    if ((t<time[i]) is True) and ((t>time[i]) is False):
        f = (i-1,time[i-1])
        break

a = abs(f[1]-t)
print(value[f[0]]-a)