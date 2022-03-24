N = int(input())
W = list(map(int, input().split()))
ans = 10**5
for i in range(1, N+1):
    ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
print(ans)
    