H, W = map(int, input().split())
ALL_NUMBERS = {'1', '2', '3', '4', '5' }
C = []
C.append(['#'] * (W+2))
for i in range(H):
    C.append(['#'] + list(input()) + ['#'])
C.append(['#'] * (W+2))

for i in range(1, H+1):
    for j in range(1, W+1):
        if C[i][j] != '.':
            continue
        s = { C[i+1][j], C[i][j+1], C[i-1][j], C[i][j-1] }
        d = ALL_NUMBERS.difference(s)            
        C[i][j] = d.pop()

for l in C[1:-1]:
    print(''.join(l[1:-1]))
