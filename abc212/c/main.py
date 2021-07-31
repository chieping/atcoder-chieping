from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 10**18

# for i in range(N):
#     j = bisect_left(B, A[i])
#     if j > 0:
#         ans = min(ans, abs(A[i] - B[j-1]))
#     if j != M:
#         ans = min(ans, abs(A[i] - B[j]))

x, y = 0, 0
while (x < N) and (y < M):
    ans = min(ans, abs(A[x] - B[y]))
    if A[x] > B[y]:
        y += 1
    else:
        x += 1

print(ans)
