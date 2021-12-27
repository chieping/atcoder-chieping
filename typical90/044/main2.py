from sys import stdin
N, Q = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
shift = 0
for _ in range(Q):
    t, x, y = map(int, stdin.readline().split())
    x -= 1
    y -= 1
    if t == 1:
        A[(x-shift)%N], A[(y-shift)%N] = A[(y-shift)%N], A[(x-shift)%N]
    elif t == 2:
        shift = (shift + 1) % N
    elif t == 3:
        print(A[(x-shift)%N])
