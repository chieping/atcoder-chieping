import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
P = list(map(int, readline().split()))
P.sort()
print(sum(P[:K]))