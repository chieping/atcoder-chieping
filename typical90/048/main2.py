import heapq
from sys import stdin
N, K = map(int, stdin.readline().split())
A = []
B = []
for i in range(N):
    a, b = map(int, stdin.readline().split())
    A.append(((a-b)*-1, -1))
    heapq.heappush(B, (-b, i))

ans = 0
for _ in range(K):
    v, i = heapq.heappop(B)
    ans += v
    if i != -1:
        heapq.heappush(B, A[i])

print(ans*-1)
