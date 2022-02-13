N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in range(N):
    av = A[a]
    for b in range(a+1, N):
        bv = A[b]
        for c in range(b+1, N):
            cv = A[c]
            for d in range(c+1, N):
                dv = A[d]
                for e in range(d+1, N):
                    ans += av+bv+cv+dv+A[e] == 1000
print(ans)