N = int(input())
A = list(map(int, input().split()))
ans = 1<<60
for bit in range(1<<(N-1)):
    xored = 0
    ored = 0
    for i in range(N):
        ored |= A[i]
        if (bit >> i) & 1:
            xored ^= ored
            ored = 0
    xored ^= ored
    ans = min(ans, xored)
print(ans)
