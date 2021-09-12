import heapq

N, M = map(int, input().split())
ans = 0

G = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    # 負の場合は必ず追加するので元から省いておく
    if c > 0:
        ans += c
    a -= 1
    b -= 1
    G[a].append((c, b))
    G[b].append((c, a))

marked = [False] * N
marked_count = 0

Q = []

marked[0] = True
marked_count = 1
for c, b in G[0]:
    heapq.heappush(Q, (c, b))

while marked_count < N:
    c, b = heapq.heappop(Q)

    if marked[b]:
        continue

    if c > 0:
        ans -= c
    
    marked[b] = True
    marked_count += 1

    for i in G[b]:
        heapq.heappush(Q, i)

print(ans)
