N = int(input())
V = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        a = V[i]
        b = V[j]
        if -1 <= (b[1] - a[1]) / (b[0] - a[0]) <= 1:
            ans += 1

print(ans)
