# WA
import sys
readline = sys.stdin.readline
N = int(readline())
S = list(map(int, readline().split()))
A = [0] * (N+2)
if N > 1:
    if S[0] > S[1]:
        A[0] = S[0]-S[1]
if N > 2:
    if S[1] > S[2]:
        A[1] = S[1]-S[2]

ok = True
for i in range(2, N+2):
    a = S[i-2] - A[i-2] - A[i-1]
    if a >= 0:
        A[i] = a
    else:
        ok = False
        break
if ok:
    print('Yes')
    print(*A)
    exit()

print('No')
