from itertools import product
N, M = map(int, input().split())
K = [0] * M
S = [[] for _ in range(M)]
for i in range(M):
    K[i], *S[i] = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
for switch in product([True, False], repeat=N):
    for i in range(M):
        cnt = 0
        for j in S[i]:
            cnt += switch[j-1]
        if cnt % 2 != P[i]:
            break
    else:
        ans += 1
print(ans)
