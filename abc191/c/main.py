from sys import stdin
H, W = map(int, stdin.readline().split())
S = [list(stdin.readline()[:-1]) for _ in range(H)]
d = ((0, 0), (0, 1), (1, 0), (1, 1))
ans = 0
for i in range(H-1):
    for j in range(W-1):
        cnt = 0
        for di, dj in d:
            if S[i+di][j+dj] == '#':
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
