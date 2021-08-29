import heapq


N, K = map(int, input().split())
A = list(map(lambda x: int(x) * -1, input().split()))
A.sort(reverse=False)
ans = 0

for i in range(K):
    m = heapq.heappop(A)
    if m >= 0:
        heapq.heappush(m)
        continue

    m *= -1
    m2 = heapq.heappop(A)
    m2 *= -1
    s = m-m2
    
    ans = ans + (m2*s+1) + (sum(range(0, s+1)))
    heapq.heappush(A, (m-s) * -1)
    heapq.heappush(A, m2 * -1)

print(ans)

        


