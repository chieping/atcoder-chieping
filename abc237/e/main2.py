from collections import deque
from heapq import heappop, heappush
N, M = map(int, input().split())
H = list(map(int, input().split()))
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    # 低い山から高い山への移動はその標高の差の分のコストがかかる
    # と言い換える。高い山から低い山への移動はコスト0
    G[u].append((max(0, H[v] - H[u]), v))
    G[v].append((max(0, H[u] - H[v]), u))

Q = []
cost = [-1] * N
done = [False] * N
cost[0] = 0
heappush(Q, (0, 0))

while len(Q):
    now_cost, now_loc = heappop(Q)
    if done[now_loc]:
        continue
    done[now_loc] = True

    for c, v in G[now_loc]:
        if cost[v] == -1 or cost[v] > cost[now_loc] + c:
            cost[v] = cost[now_loc] + c
            heappush(Q, (cost[v], v))

print(H[0] - min(H[i] + cost[i] for i in range(N)))