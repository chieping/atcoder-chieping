N = int(input())
C = []
S = []
F = []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N-1):
    ans = 0
    for j in range(i, N-1):
        if ans < S[j]:
            ans = S[j]
        if (ans-S[j]) % F[j] > 0:
            ans += F[j] - (ans-S[j]) % F[j]
        ans += C[j]
    print(ans)
print(0)