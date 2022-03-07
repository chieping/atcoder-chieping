from pprint import pprint
import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
A = list(map(int, readline().split()))
A = [a - 1 for a in A]
visited = [-1] * N
visited[0] = 0
k = K
now = 0
while k > 0:
    k -= 1
    nxt = A[now]
    if visited[nxt] != -1:
        cycle = K - k - visited[nxt]
        k %= cycle
    visited[nxt] = K - k
    now = nxt

print(now+1)