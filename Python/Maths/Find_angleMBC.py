# https://courses.lumenlearning.com/boundless-algebra/chapter/trigonometry-and-right-triangles/
# https://www.hackerrank.com/challenges/find-angle/forum

from math import sqrt, atan2, atan, degrees

ab = 10 # int(input())
bc = 10 # int(input())

abc = 90 # deg

a = ab
b = bc
c = sqrt(a**2+b**2)
print(a,b,c)

# right angle triangle has a angle of 90 degree
# a**2 + b**2 == c**2 (pythogorus theorem)
# opp = side of the triange (straight)    => (opp)
# adjacent = base of the triangle         => (adj)
# hypotense = side(slope) of the triangle => (hypo)

# trigonometry formulae
# sin = opp / hypo
# cos = adj / hypo
# tan = opp / adj


# tan (t) = opp/ adj
# acute angle => a = atan(opp/adj)
t = atan2(a,b)
acute = round(degrees(t))
print(f'%d{chr(176)}' %acute)
