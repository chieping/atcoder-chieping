from math import atan2, cos, pi, sin, sqrt
a, b, d = map(int, input().split())
theta = atan2(b, a)
r = sqrt(a*a+b*b)
d *= pi/180
x = cos(theta+d)*r
y = sin(theta+d)*r
print(x, y)
