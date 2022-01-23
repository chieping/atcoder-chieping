import heapq
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
A = [-a for a in A]
A.sort()
H = [A[0]]
ans = 0
for a in A[1:]:
    ans += heapq.heappop(H)
    heapq.heappush(H, a)
    heapq.heappush(H, a)
print(-ans)
