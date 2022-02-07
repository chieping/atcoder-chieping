# WIP
from collections import deque


N, X, Y = map(int, input().split())
X -= 1
Y -= 1
INF = 10**18
ans = []
for sv in range(N):
    dist = [INF] * N
    q = deque()
