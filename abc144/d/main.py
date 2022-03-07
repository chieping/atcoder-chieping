from math import atan2
import math
a, b, x = map(int, input().split())
S = x / a
if S >= a * b / 2:
    t = a * b - S
    h = t * 2 / a
    rad = atan2(h, a)
else:
    w = 2 * S / b
    rad = atan2(b, w)
deg = rad / 2 / math.pi * 360
print(deg)