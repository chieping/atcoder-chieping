N = int(input())
P = list(map(int, input().split()))
expected = sorted(P)
ans = expected == P
for i in range(N-1):
    for j in range(i+1, N):
        Q = P.copy()
        Q[i], Q[j] = Q[j], Q[i]
        if expected == Q:
            ans = True
print('YES' if ans else 'NO')