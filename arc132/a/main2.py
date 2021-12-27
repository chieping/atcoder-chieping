# TLE
n = int(input())
R = sorted(list(zip(map(int, input().split()), range(n))), reverse=True)
C = sorted(list(zip(map(int, input().split()), range(n))))
G = [[-1]*n for _ in [0]*n]
cols = []
for i in range(n):
    max_row = R[i][1]
    for col in cols:
        G[max_row][col] = 0
    min_col = C[i][1]
    cols.append(min_col)

ans = []
q = int(input())
for _ in [0]*q:
    r, c = map(int, input().split())
    if G[r-1][c-1] == 0:
        ans.append('.')
    else:
        ans.append('#')
print(''.join(ans))
