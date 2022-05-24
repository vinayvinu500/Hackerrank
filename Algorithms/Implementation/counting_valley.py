# counting valley => https://www.hackerrank.com/challenges/counting-valleys/problem
import matplotlib.pyplot as plt

# values => {D,U}
d = {'D':-1,'U':+1}

# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
arr = (['D','D','U','U','U','U','D','D'],['U','D','D','D','U','D','U','U'],['D','U','D','D','U','U','U','U','D','D','D'],['U','D','D','D','U','D','U','U'])
# testcase => output = 10
ar = ['D', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'D', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'D', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'U', 'D', 'U', 'U', 'U', 'D', 'U', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'U', 'U', 'D', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U']

def show(st):
	plt.axhline(y=0,color='r',linestyle='-')
	plt.plot(st)
	plt.show()

def countingValleys(steps, path):
    vl = 0 # valley count
    sl = 0 # sea level
    st = [0,]
    for i in path:
    	sl += d[i]
    	st.append(sl)

    print(st[:50])
    
    c = 0
    for i in range(len(st)):
    	walk = st[i:i+2]
    	if walk == [0,-1]:
    		if c == 0:
    			c = 1
    	if walk == [-1,0]:
    		if c == 1:
    			vl += 1
    			c = 0
    print(vl)
    


# countingValleys(len(arr[0]),arr[0])
# countingValleys(len(arr[1]),arr[2])
# countingValleys(len(arr[2]),arr[2])
# countingValleys(len(arr[3]),arr[3])
countingValleys(len(ar),ar)



"""
approach => -1 to 0 => count++

pattern => one valley => [0,-1] ---- [-1,0]
1. downward => 0,-1 
2. upward => -1,0  
"""

