from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
A.append(-1)

whole = (N * (N-1)) // 2

D = defaultdict(lambda: 0)

for a in A:
    D[a] = D[a] + 1

dup = 0
for key in D:
    if D[key] > 1:
        dup += D[key] * (D[key] -1) // 2

print(whole - dup)
