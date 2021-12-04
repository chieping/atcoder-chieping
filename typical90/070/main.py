N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0
X.sort()
Y.sort()
mid_x = X[N//2]
mid_y = Y[N//2]
ans += sum([abs(x - mid_x) for x in X])
ans += sum([abs(y - mid_y) for y in Y])
print(ans)
