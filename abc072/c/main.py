from typing import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
cnt.update([a - 1 for a in A])
cnt.update([a + 1 for a in A])
print(max(cnt.values()))