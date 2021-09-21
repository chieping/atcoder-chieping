import math

N = int(input())
x0, y0 = map(float, input().split())
x, y = map(float, input().split())

qx = (x0 + x) / 2
qy = (y0 + y) / 2

rad = 2 * math.pi / N

# 回転行列
ansx = qx + (x0-qx) * math.cos(rad) - (y0-qy) * math.sin(rad)
ansy = qy + (x0-qx) * math.sin(rad) + (y0-qy) * math.cos(rad)

print(ansx, ansy)
