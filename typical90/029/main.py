# 座標圧縮
# TLE 部分点のみ、すべてACするには遅延セグメント木を使う

import heapq

W, N = map(int, input().split())
LR = []
heap = []
for _ in range(N):
    l, r = map(int, input().split())
    l -= 1; r -= 1
    LR.append((l, r))
    heapq.heappush(heap, l)
    heapq.heappush(heap, r)
Len = len(heap)
H = [0] * Len
i_map = dict()
j = 0
while len(heap):
    i = heapq.heappop(heap)
    i_map[i] = j
    j += 1

for l, r in LR:
    li = i_map[l]
    ri = i_map[r]
    M = max(H[li:ri+1])
    for i in range(li, ri+1):
        H[i] = M+1
    print(M+1)
