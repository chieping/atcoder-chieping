from itertools import permutations
import sys
readline = sys.stdin.readline
N = int(readline())
P = tuple(map(int, readline().split()))
Q = tuple(map(int, readline().split()))
ALL = list(permutations(range(1, N+1)))
print(abs(ALL.index(P)-ALL.index(Q)))