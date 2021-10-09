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
    res.sort()
    for i in range(0, 2*N, 2):
        a = A[res[i][1]][j]
        b = A[res[i+1][1]][j]
        s = janken(a, b)
        res[i][0] -= s[0]
        res[i+1][0] -= s[1]

res.sort()
for j in range(len(res)):
    print(res[j][1]+1)
