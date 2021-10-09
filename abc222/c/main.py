N, M = map(int, input().split())
A = [list(input()) for i in range(2*N)]
# (勝数, 番号)
res = [[0, i] for i in range(0, 2*N)]

def janken(a, b):
    if a == b:
        return (0, 0)
    elif a == 'G' and b == 'C':
        return (1, 0)
    elif a == 'G' and b == 'P':
        return (0, 1)
    elif a == 'C' and b == 'P':
        return (1, 0)
    elif a == 'C' and b == 'G':
        return (0, 1)
    elif a == 'P' and b == 'G':
        return (1, 0)
    elif a == 'P' and b == 'C':
        return (0, 1)


for j in range(M):
    for i in range(0, 2*N, 2):
        p1 = res[i][1]
        p2 = res[i+1][1]
        s1, s2 = janken(A[p1][j], A[p2][j])
        res[i][0] -= s1
        res[i+1][0] -= s2
    res.sort()

for _, i in res:
    print(i+1)
