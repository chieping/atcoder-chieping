import heapq
K, T = map(int, input().split())
A = list(map(int, input().split()))
h = [(-a, i) for i, a in enumerate(A) if a > 0]
heapq.heapify(h)
last = -1
ans = 0

while len(h) > 0:
    e1 = heapq.heappop(h)
    if len(h) == 0:
        if last == e1[1]:
            ans += 1
        if e1[0] < -1:
            heapq.heappush(h, (e1[0]+1, e1[1]))
        last = e1[1]
    else:
        e2 = heapq.heappop(h)
        last = e2[1]
        if e1[0] < -1:
            heapq.heappush(h, (e1[0]+1, e1[1]))
        if e2[0] < -1:
            heapq.heappush(h, (e2[0]+1, e2[1]))

print(ans)
