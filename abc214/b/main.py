S, T = map(int, input().split())
M = 100
ans = 0
for a in range(M + 1):
    for b in range(M + 1):
        for c in range(M + 1):
            if ((a + b + c) <= S) and ((a * b * c) <= T):
                ans += 1

print(ans)
