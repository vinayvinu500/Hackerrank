# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

mean = 70
sd = 10

#P(X>80)
x = 80
z = (x - mean) / sd

Z = 1.0
A = 0.84134

p_x_80 = 1 - A
print(round(p_x_80,2))
#P(X>=60)
x = 60
z = (x - mean) / sd
Z = -1.0
A = 
#P(X<60)