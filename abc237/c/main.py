S = input()
n = len(S)

firstAcount = 0
lastAcount = 0
for i in range(n):
    if S[n-1-i] == 'a':
        lastAcount += 1
    else:
        break
for i in range(n):
    if S[i] == 'a':
        firstAcount += 1
    else:
        break

SS = S[:n-(lastAcount-firstAcount)]
print('Yes' if SS == SS[::-1] else 'No')
