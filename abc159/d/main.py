from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)

all = 0
for n in C.values():
    all += n * (n-1) // 2

for a in A:
    n = C[a]
    ans = all - n + 1
    print(ans)
