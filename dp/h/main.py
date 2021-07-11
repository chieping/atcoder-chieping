H, W = map(int, input().split())

A = [list(input()) for i in range(H)]

cnt = [[0] * W for i in range(H)]

cnt[0][0] = 1

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            continue
        if i > 0:
            cnt[i][j] += cnt[i-1][j]
        if j > 0:
            cnt[i][j] += cnt[i][j-1]
        cnt[i][j] %= 1_000_000_007

print(cnt[H-1][W-1])
