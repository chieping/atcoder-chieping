from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
S = [0] * N
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

_max = -10**8
move = 0
cur = 0
ans = 0
for i in range(N):
    _max = max(_max, S[i])
    move += A[i]
    ans = max(ans, cur + _max)
    cur += move

print(ans)

