from collections import deque
from pprint import pprint
import sys
readline = sys.stdin.readline
H, W, N =  map(int, readline().split())
sx, sy = map(int, readline().split())
gx, gy = map(int, readline().split())
shougaibutu = [tuple(map(int, readline().split())) for _ in range(N)]

Xlist = []
Ylist = []

for x, y in shougaibutu:
    Xlist.append((x, y))




Q = deque()
Q.append((sx, sy))

while len(Q) > 0:
    x, y = Q.popleft()
    