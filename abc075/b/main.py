H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans[i][j] = '#'
            continue
        res = 0
        for di in range(i-1, i+2):
            for dj in range(j-1, j+2):
                if not 0 <= di < H: continue
                if not 0 <= dj < W: continue
                res += S[di][dj] == '#'
        ans[i][j] = res

for line in ans:
    print(*line, sep='')
