# WA
# 全頂点を始点としてダイクストラし、
# 一度も使わなかった辺は削除できるかと
# 思ったが、、

import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

edge = [[] for _ in range(N)]
used = set()

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((c, b, i))
    edge[b].append((c, a, i))

def dai(start):
    dist = [-1] * N
    done = [False] * N
    Q = []
    # 距離、現在地
    heapq.heappush(Q, (0, start, -1))
    dist[start] = 0
    while len(Q) > 0:
        d, v, i = heapq.heappop(Q)
        if done[v]:
            continue
        done[v] = True
        used.add(i)

        for c, nxt, j in edge[v]:
            if dist[nxt] == -1 or dist[nxt] > dist[v] + c:
                dist[nxt] = dist[v] + c
                heapq.heappush(Q, (dist[nxt], nxt, j))

for k in range(N):
    dai(k)

used.remove(-1)
print(M - len(used))
