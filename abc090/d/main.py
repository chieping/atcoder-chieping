N, K = map(int, input().split())

def calc(b):
    fans = 0
    fans += (b-K) * (N//b)
    mod = N % b
    if mod != 0:
        fans += max(0, mod - (K-1))
    return fans

def solve():
    if K == 0:
        return N*N
    ans = 0
    for b in range(2, N+1):
        if b - 1 < K: continue
        ans += calc(b)
    return ans

print(solve())
