import sys
readline = sys.stdin.readline
N = int(readline())
S = list(readline()[:-1])
van = False
ans = []
for i in range(1, N):
    if van == True:
        van = False
        continue
    prev = S[i-1]
    curr = S[i]
    if prev == 'B' and curr == 'B':
        ans.append('A')
        van = True
    elif prev == 'B' and curr == 'A':
        ans.append('A')
        S[i] = 'B'
    else:
        ans.append(prev)
if not van:
    ans.append(S[-1])
print(''.join(ans))