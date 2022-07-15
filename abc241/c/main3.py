import sys
input = sys.stdin.readline
N = int(input())
S = [input()[:-1] for _ in range(N)]
DX = [1, 0, 1, 1]
DY = [0, 1, 1, -1]

def f(i, j, dx, dy):
    cnt = 0
    for k in range(6):
        x = i+dx*k
        y = j+dy*k
        if not(x < N and 0 <= y < N):
            return False
        cnt += S[x][y] == '#'
    return cnt >= 4

ans = False
for i in range(N):
    for j in range(N):
        for dx, dy in zip(DX, DY):
            ans |= f(i, j, dx, dy)
print('Yes' if ans else 'No')
