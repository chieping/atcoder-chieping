# import io
# import sys
# _INPUT = """\
# 41 7 46
# 26 89 2
# 78 92 8
# 5
# 6
# 45
# 16
# 57
# 17
# """
# sys.stdin = io.StringIO(_INPUT)
# ------

A = []

for _ in range(0, 3):
    row  = list(map(int, input().split()))
    A.append(row)

M = [[False, False, False], [False, False, False], [False, False, False]]

N = int(input())

for _ in range(0, N):
    b = int(input())

    for i in range(0, 3):
        for j in range(0, 3):

            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(0, 3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    bingo = True
    
if M[2][0] and M[1][1] and M[0][2]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")

