N = int(input())
V = [list(map(int, input().split())) for i in range(N)]
ans = 0
x = 0
y = 1
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            # 座標平面上の三角形の面積の公式を使う
            if (V[c][x]-V[a][x])*(V[b][y]-V[a][y])-(V[b][x]-V[a][x])*(V[c][y]-V[a][y]) != 0:
                ans += 1
print(ans)
