from collections import Counter
import sys
sys.setrecursionlimit(10**6)

N = int(input())
C = Counter(map(int, input().split()))

dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

def f(c1, c2, c3):
    sm = c1+c2+c3
    if sm == 0:
        return 0
    if dp[c1][c2][c3] > 0:
        return dp[c1][c2][c3]
    P1 = 0
    P2 = 0
    P3 = 0
    if c1: P1 = f(c1-1, c2,   c3  )*c1
    if c2: P2 = f(c1+1, c2-1, c3  )*c2
    if c3: P3 = f(c1,   c2+1, c3-1)*c3

    dp[c1][c2][c3] = (N+P1+P2+P3) / sm
    return (N+P1+P2+P3) / sm

print(f(C[1], C[2], C[3]))
