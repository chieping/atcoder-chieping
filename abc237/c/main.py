import sys
readline = sys.stdin.readline

S = readline()[:-1]
l = len(S)

if S == S[::-1]:
    print('Yes')
    exit()

firstAcount = 0
lastAcount = 0
for i in range(l):
    if S[l-1-i] == 'a':
        lastAcount += 1
    else:
        break
for i in range(l):
    if S[i] == 'a':
        firstAcount += 1
    else:
        break

if firstAcount > lastAcount:
    print('No')
else:
    SS = S[:l-(lastAcount-firstAcount)]
    print('Yes' if SS == SS[::-1] else 'No')
