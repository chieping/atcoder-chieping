N, Q = map(int, input().split())
A = list(map(int, input().split()))
offset = 0
for _ in range(Q):
    t, x, y = map(int, input().split())
    x = (x-1-offset) % N
    y = (y-1-offset) % N
    if t == 1:
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        offset = (offset + 1) % N
    elif t == 3:
        print(A[x])
