N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a-1 for a in A]
# B=持ってない人
B = set(range(N)) - set(A)
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 0
for i in B:
    lans = 10**18
    for k in A:
        lans = min(lans, (X[k]-X[i])**2 + (Y[k]-Y[i])**2)
    ans = max(ans, lans)
print(ans**(1/2))
