from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = set(k for k, v in Counter(A).items() if v == 1)
A.sort()
Max = A[-1]
C = set()

for a in A:
    j = 2
    while a*j <= Max:
        C.add(a*j)
        j += 1

print(len(B - C))