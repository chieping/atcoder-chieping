N = int(input())
S = list(input())
Q = int(input())

rev = False
for i in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if rev:
            a = (a+N)%(N*2)
            b = (b+N)%(N*2)
        S[a], S[b] = S[b], S[a]
    else:
        rev = not rev

print(''.join(S[N:] + S[0:N] if rev else S))
