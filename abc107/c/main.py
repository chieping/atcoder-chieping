N, K = map(int, input().split())
X = list(map(int, input().split()))
P = [0]
N = []
for x in X:
    if x > 0:
        P.append(x)
    else:
        N.append(-x)
N.append(0)
N = N[::-1]

ans = 10**18
for i in range(K+1):
    if K-i >= len(P): continue
    if i >= len(N): continue
    ans = min(ans, P[K-i] + N[i] + min(P[K-i], N[i]))
print(ans)
