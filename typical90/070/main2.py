import sys
readline = sys.stdin.readline
N = int(readline())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, readline().split())

cx = sorted(X)[N//2]
cy = sorted(Y)[N//2]

ans = 0
ans += sum(abs(cx - x) for x in X)
ans += sum(abs(cy - y) for y in Y)
print(ans)
