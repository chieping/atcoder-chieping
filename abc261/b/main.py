N = int(input())
A = [list(input()) for _ in range(N)]
ans = False

for i in range(N):
    for j in range(N):
        if i == j:
            ans |= A[i][j] != '-'
        if A[i][j] == 'W':
            ans |= A[j][i] != 'L'
        elif A[i][j] == 'L':
            ans |= A[j][i] != 'W'
        elif A[i][j] == 'D':
            ans |= A[j][i] != 'D'

print('incorrect' if ans else 'correct')