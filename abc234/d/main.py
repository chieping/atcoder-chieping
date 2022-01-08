import heapq
from sys import stdin
N, K = map(int, stdin.readline().split())
P = list(map(int, stdin.readline().split()))
H = P[:K].copy()
heapq.heapify(H)
ans = H[0]
print(ans)
for i in range(K, N):
    if P[i] > ans:
        heapq.heappushpop(H, P[i])
        ans = H[0]
    print(ans)
