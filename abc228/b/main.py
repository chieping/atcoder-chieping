N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))
T = [False] * (N+1)

ans = 0
i = X
while T[i] == False:
    T[i] = True
    ans += 1
    i = A[i]
print(ans)


