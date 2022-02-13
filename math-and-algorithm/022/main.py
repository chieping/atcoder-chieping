from collections import Counter
import sys
readline = sys.stdin.readline
N = int(readline())
C = Counter(list(map(int, readline().split())))
ans = 0
for i in range(1, 50000):
    x = C[i]
    y = C[100000-i]
    ans += x * y

if C[50000] > 1:
    ans += C[50000] * (C[50000]-1) // 2
print(ans)