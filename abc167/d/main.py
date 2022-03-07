from pprint import pprint
import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
A = [0] + list(map(int, readline().split()))
visited = [-1] * (N+1)
visited[1] = 0
k = K
now = 1
while k > 0:
    k -= 1
    nxt = A[now]
    if visited[nxt] != -1 and k > N:
        cycle = K - k - visited[nxt]
        k %= cycle
    visited[nxt] = K - k
    now = nxt

print(now)