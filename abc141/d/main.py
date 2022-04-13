import heapq
N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
heapq.heapify(A)
for _ in range(M):
    a = heapq.heappop(A)
    a = -a
    heapq.heappush(A, a // 2 * -1)
print(sum(A) * -1)