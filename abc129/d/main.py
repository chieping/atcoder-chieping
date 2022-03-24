from pprint import pprint
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
S = [input()[:-1] for _ in range(H)]
T = list(zip(*S))

# 縦横それぞれ連続した区間の数を求める
horizon = [[0] * W for _ in range(H)]
for i in range(H):
    cur = 0
    l = 0
    r = 0
    while r < W:
        if S[i][r] == '#':
            horizon[i][l:r] = [cur] * (r-l)
            cur = 0
            l = r+1
        else:
            cur += 1
        r += 1
    horizon[i][l:r] = [cur] * (r-l)
# pprint(horizon)

vertical = [[0] * H for _ in range(W)]
for i in range(W):
    cur = 0
    l = 0
    r = 0
    while r < H:
        if T[i][r] == '#':
            vertical[i][l:r] = [cur] * (r-l)
            cur = 0
            l = r+1
        else:
            cur += 1
        r += 1
    vertical[i][l:r] = [cur] * (r-l)
vertiacal = list(zip(*vertical))

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, horizon[i][j] + vertiacal[i][j] - 1)
print(ans)