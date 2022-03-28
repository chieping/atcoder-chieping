# 解説AC
# 最短距離はBFS
# グラフと見られるか考える
from collections import deque
import sys
input = sys.stdin.readline
M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)
P = list(map(int, input().split()))
s = [9] * 9
for i in range(8):
    s[P[i]-1] = i+1

def to_s(list):
    return ''.join(str(i) for i in list)

s = to_s(s)
Q = deque()
Q.append(s)
mp = {}
mp[s] = 0

while len(Q):
    s = Q.popleft()
    v = s.index('9')
    for u in edge[v]:
        t = list(s)
        t[u], t[v] = t[v], t[u]
        t = to_s(t)
        if t in mp:
            continue
        mp[t] = mp[s] + 1
        Q.append(t)

print(mp.get('123456789', -1))
