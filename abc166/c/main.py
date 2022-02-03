import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
H = list(map(int, readline().split()))
good = [True] * N
for _ in range(M):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    if H[a] == H[b]:
        good[a] = False
        good[b] = False
    if H[a] > H[b]:
        good[b] = False
    else:
        good[a] = False
print(sum(good))
