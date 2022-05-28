from itertools import accumulate
N, Q = map(int, input().split())
S = input()
C = [0] * (N+1)

a = False
for i, c in enumerate(S, 1):
    if a and c == 'C':
        C[i] = 1
    a = c == 'A'
C = list(accumulate(C))

for _ in range(Q):
    l, r = map(int, input().split())
    ans = C[r] - C[l]
    print(ans)
