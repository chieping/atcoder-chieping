N = int(input())
A = [0] + list(map(int, input().split()))
ans = [False] * (N+1)
for i in range(N, 0, -1):
    x = 0
    for j in range(i, N+1, i):
        x ^= ans[j]
    ans[i] = A[i] ^ x
ans = [i for i in range(1, N+1) if ans[i] == 1]
print(len(ans))
print(*ans)
