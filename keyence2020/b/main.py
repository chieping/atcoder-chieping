N = int(input())
X = []
L = []
for _ in range(N):
    x, l = map(int, input().split())
    X.append(x)
    L.append(l)
ps = [(X[i] + L[i], X[i] - L[i]) for i in range(N)]
ps.sort()
ans = 0
cur = -10**10
for i in range(N):
    if cur <= ps[i][1]:
        ans += 1
        cur = ps[i][0]
print(ans)
