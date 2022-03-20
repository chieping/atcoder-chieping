from pprint import pprint
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def cnt(lx, ly, rx, ry):
    return sum(lx <= x <= rx and ly <= y <= ry for x, y in XY)

X = [0] * N
Y = [0] * N
for i in range(N):
    X[i] = XY[i][0]
    Y[i] = XY[i][1]    
X.sort()
Y.sort()

ans = 10**20
for i in range(N):
    for j in range(i+1, N):
        for k in range(N):
            for l in range(k+1, N):
                if cnt(X[i], Y[k], X[j], Y[l]) >= K:
                    ans = min(ans, (X[j] - X[i]) * (Y[l] - Y[k]))
print(ans)