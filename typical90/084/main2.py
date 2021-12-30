from sys import stdin
N = int(stdin.readline())
S = list(stdin.readline())[:-1] + ['.']
ans = N*(N-1)//2
char = ''
seq = 1
for i in range(N+1):
    if S[i] == char:
        seq += 1
    else:
        ans -= seq*(seq-1)//2
        char = S[i]
        seq = 1
print(ans)
