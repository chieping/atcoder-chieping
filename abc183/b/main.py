from sys import stdin
sx, sy, gx, gy = map(int, stdin.readline().split())
katamuki = (gy-(-sy)) / (gx-sx)
print(sy / katamuki + sx)
