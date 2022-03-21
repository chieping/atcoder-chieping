from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)

# 文字列Sに関する良いパス、かつ最後がlstのパス
# のうち最短のものの長さ
opt = [[0] * 17 for _ in [0] * (1<<17)]
que = deque()

for i in range(N):
    opt[1<<i][i] = 1
    que.append((1<<i, i))

while len(que) > 0:
    msk, lst = que.popleft()
    for to in edge[lst]:
        msk2 = msk ^ (1<<to)
        if opt[msk2][to] == 0:
            opt[msk2][to] = opt[msk][lst] + 1
            que.append((msk2, to))

ans = 0
for msk in range(1, 1<<N):
    mi = 10**18
    for lst in range(N):
        mi = min(mi, opt[msk][lst])
    ans += mi

print(ans)
