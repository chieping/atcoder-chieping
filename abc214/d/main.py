from collections import deque

N = int(input())
G = []
for i in range(N):
    G.append([])

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

ans = 0

# for i in range(N):
#     for j in range(i+1, N):
#         # from i to j の最短パスの辺の重みの最大値を足していく
#         Q = deque()
#         min_path = 10**18
#         w_max = 0
#         Q.append((i, 0, 0)) # 現在地, 辺の最大値, 辿ってきた経路数
#         while len(Q) > 0:
#             l, w_m, path = Q.popleft()
#             if min_path < path:
#                 break
#             if l == j:
#                 w_max = max(w_max, w_m)
#                 min_path = path 
#             else:
#                 for g in G[l]:
#                     Q.append((g[0], max(w_m, g[1]), path+1))
#         ans += w_max

dp = [[0]* N for i in range(N)]





print(ans)
