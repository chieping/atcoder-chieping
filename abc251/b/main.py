N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = set()
for i in range(N):
    a1 = A[i]
    if a1 <= W:
        ans.add(a1)

    for j in range(i+1, N):
        a2 = a1 + A[j]
        if a2 <= W:
            ans.add(a2)

        for k in range(j+1, N):
            a3 = a2 + A[k]
            if a3 <= W:
                ans.add(a3)

print(len(ans))