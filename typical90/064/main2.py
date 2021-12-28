from sys import stdin
N, Q = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
dist = [A[i+1]-A[i] for i in range(N-1)]
ans = sum(map(abs, dist))
for _ in range(Q):
    l, r, v = map(int, stdin.readline().split())
    l -= 1
    r -= 1
    if l > 0:
        ans -= abs(dist[l-1])
        dist[l-1] = dist[l-1] + v
        ans += abs(dist[l-1])
    if r < N-1:
        ans -= abs(dist[r])
        dist[r] = dist[r] - v
        ans += abs(dist[r])
    print(ans)
