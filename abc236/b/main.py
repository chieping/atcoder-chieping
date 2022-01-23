from collections import Counter
import sys
readline = sys.stdin.readline
N = int(readline())
A = Counter(map(int, readline().split()))

for k, cnt in A.items():
    if cnt == 3:
        print(k)