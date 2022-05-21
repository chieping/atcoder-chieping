# TLE
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
values = list(Counter(A).values())
Len = len(values)
ans = 0
Sum = N
for i, iv in enumerate(values):
    m_sum = iv
    for j in values[i+1:]:
        m_sum += j
        ans += iv * j * (Sum-m_sum)

print(ans//2)