from bisect import bisect_left
N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

now = 0
round_trip = 0

while True:
    # a->b
    ai = bisect_left(A, now)
    if ai == N:
        break
    now = A[ai] + X

    # b->a
    bi = bisect_left(B, now)
    if bi == M:
        break
    now = B[bi] + Y
    round_trip += 1

print(round_trip)
