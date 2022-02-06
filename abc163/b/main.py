import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
A = list(map(int, readline().split()))
ans = N -sum(A)
print(ans if ans >= 0 else -1)