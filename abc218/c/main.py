N = int(input())
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(N)]

def rotate(arr):
    return [i[::-1] for i in zip(*arr)]

for _ in range(4):
    S = rotate(S)
    while True:
        if not '#' in S[0]:
            S.pop(0)
        else:
            break

for _ in range(4):
    T = rotate(T)
    while True:
        if not '#' in T[0]:
            T.pop(0)
        else:
            break

for _ in range(4):
    T = rotate(T)
    if S == T:
        print('Yes')
        exit()
print('No')
