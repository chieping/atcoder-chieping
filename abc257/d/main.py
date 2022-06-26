import sys
input = sys.stdin.readline
N = int(input())
X, Y, P = [], [], []
for _ in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)
INF = float('inf')

ng = 0
ok = 10**10

while abs(ng-ok) > 1:
    mid = (ng+ok)//2
    d = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist = abs(X[i]-X[j]) + abs(Y[i]-Y[j])
            if mid*P[i] >= dist:
                d[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] |= d[i][k] and d[k][j]
    for i in range(N):
        if all(d[i]):
            # print('ok', mid)
            ok = mid
            break
    else:
        # print('ng', mid)
        ng = mid
print(ok)