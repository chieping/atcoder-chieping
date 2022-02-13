import sys
readline = sys.stdin.readline
N, L, W = map(int, readline().split())
A = [-W] + list(map(int, readline().split())) + [L]
# まだ被さっていない領域の長さの配列を作る
B = []
for i in range(1, N+2):
    prev = A[i-1]
    curr = A[i]
    if curr - prev - W > 0:
        B.append(curr - prev - W)
ans = 0
for b in B:
    ans += (b+W-1) // W
print(ans)
