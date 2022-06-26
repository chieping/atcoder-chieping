import sys
input = sys.stdin.readline
N = int(input())
X, Y, P = [], [], []
for _ in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)
S = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        S[i][j] = (abs(X[i]-X[j])+abs(Y[i]-Y[j])+P[i]-1)//P[i]
for k in range(N):
    for i in range(N):
        for j in range(N):
            S[i][j] = min(S[i][j], max(S[i][k], S[k][j]))
print(min(max(S[i]) for i in range(N)))
