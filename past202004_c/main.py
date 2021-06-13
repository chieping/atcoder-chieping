
n = int(input())

S = []

for i in range(0, n):
    si = input()
    si = list(si)
    S.append(si)

for i in range(n - 2, -1, -1):
    
    for j in range(1, 2 * n - 1):
        if S[i][j] == '#':
            if S[i+1][j-1] == 'X':
                S[i][j] = 'X'
            if S[i+1][j] == 'X':
                S[i][j] = 'X'
            if S[i+1][j+1] == 'X':
                S[i][j] = 'X'

for i in range(0, n):
    S[i] = ''.join(S[i])
    print(S[i])
