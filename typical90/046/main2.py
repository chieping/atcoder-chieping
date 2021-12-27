from collections import Counter
from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
C = list(map(int, stdin.readline().split()))

A46 = Counter(i % 46 for i in A)
B46 = Counter(i % 46 for i in B)
C46 = Counter(i % 46 for i in C)

ans = 0
for ak, av in A46.items():
    for bk, bv in B46.items():
        for ck, cv in C46.items():
            if (ak + bk + ck) % 46 == 0:
                ans += av * bv * cv
print(ans)
