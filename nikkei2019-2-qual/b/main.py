from collections import Counter
MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
if D[0] != 0:
    print(0)
    exit()

C = Counter(D)
if C[0] > 1:
    print(0)
    exit()

ans = 1
parent = 1
M = max(C.keys())
for i in range(1, M+1):
    ans = ans * pow(parent, C[i], MOD) % MOD
    parent = C[i]
print(ans)
