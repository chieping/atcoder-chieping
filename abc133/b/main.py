N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        dist_sq = sum((X[i][k]-X[j][k])**2 for k in range(D))
        if int(dist_sq**(1/2)) ** 2 == dist_sq:
            ans += 1
print(ans)