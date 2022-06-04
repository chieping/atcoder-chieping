import sys
input = sys.stdin.readline
N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

# マンハッタン距離は45度回転
XX = [x-y for x, y in zip(X, Y)]
YY = [x+y for x, y in zip(X, Y)]

ans = max(abs(max(XX)-min(XX)), abs(max(YY)-min(YY)))
print(ans)
