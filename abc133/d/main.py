N = int(input())
A = list(map(int, input().split()))
Sum = sum(A)
ans = [0] * N

def solve(n):
    ret = Sum
    for i in range(n+1, n+N-1, 2):
        ret -= 2*A[i%N]
    return ret

ans = [0] * N
ans[0] = solve(0)
for i in range(1, N):
    ans[i] = (A[i-1] - ans[i-1]//2)*2
print(*ans)
