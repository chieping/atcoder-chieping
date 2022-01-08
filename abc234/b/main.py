from itertools import combinations
from sys import stdin
N = int(stdin.readline())
X = []
Y = []
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    X.append(x)
    Y.append(y)

ans = 0
for i, j in combinations(range(N), 2):
    ans = max(ans, (abs(X[i]-X[j])**2 + abs(Y[i]-Y[j])**2)**(1/2))

print(ans)
