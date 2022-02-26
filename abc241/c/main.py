import sys
readline = sys.stdin.readline
N = int(readline())
S = [list(readline()[:-1]) for _ in range(N)]

def f(i, j):
    x = i
    y = j
    b = 0
    r = 2
    # R
    while r >= 0 and y < N:
        if S[x][y] == '#':
            b += 1
        else:
            b += 1
            r -= 1
        if b == 6 and r >= 0:
            return True
        y += 1

    # D
    x = i
    y = j
    b = 0
    r = 2
    while r >= 0 and x < N:
        if S[x][y] == '#':
            b += 1
        else:
            b += 1
            r -= 1
        if b == 6 and r >= 0:
            return True
        x += 1

    # RD
    x = i
    y = j
    b = 0
    r = 2
    while r >= 0 and x < N and y < N:
        if S[x][y] == '#':
            b += 1
        else:
            b += 1
            r -= 1
        if b == 6 and r >= 0:
            return True
        x += 1
        y += 1

    # LD
    x = i
    y = j
    b = 0
    r = 2
    while r >= 0 and x < N and y >= 0:
        if S[x][y] == '#':
            b += 1
        else:
            b += 1
            r -= 1
        if b == 6 and r >= 0:
            return True
        x += 1
        y -= 1

    return False

for i in range(N):
    for j in range(N):
        if f(i, j):
            print('Yes')
            exit()
print('No')