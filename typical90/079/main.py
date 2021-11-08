H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
ans = 0
for i in range(H-1):
    for j in range(W-1):
        diff = B[i][j] - A[i][j]
        A[i][j] += diff
        A[i+1][j] += diff
        A[i][j+1] += diff
        A[i+1][j+1] += diff
        ans += abs(diff)
if A == B:
    print('Yes')
    print(ans)
else:
    print('No')
