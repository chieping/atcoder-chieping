A, B, K = map(int, input().split())
C = [[0] * 61 for i in range(61)]
C[0][0] = 1
for i in range(1, 61):
    C[i][0] = 1
    for j in range(1, i+1):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

def solve(i, j, k):
    if i == 0:
        return 'b'*j
    if j == 0:
        return 'a'*i
    if C[i+j-1][i-1] >= k:
        return 'a' + solve(i-1, j, k)
    else:
        return 'b' + solve(i, j-1, k-C[i+j-1][i-1])

print(solve(A, B, K))
