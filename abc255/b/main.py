import math


N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a-1 for a in A]
# B=持ってない人
B = set(range(N)) - set(A)
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = [10**18] * N
for i in range(K):
    k = A[i]
    ans_l = 0
    for j in range(N):
        if j in B:
            # print(k, j, math.sqrt(((X[k] - X[j])**2) + ((Y[k] - Y[j])**2)))
            ans[j] = min(ans[j], math.sqrt(((X[k] - X[j])**2) + ((Y[k] - Y[j])**2)))
        else:
            ans[j] = 0

print(max(ans))