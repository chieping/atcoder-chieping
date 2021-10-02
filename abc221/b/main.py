S = input()
T = input()

if S==T:
    print('Yes')
    exit()

for i in range(len(S) - 1):
    SS = list(S)
    t = SS[i]
    SS[i] = SS[i+1]
    SS[i+1] = t
    if ''.join(SS) == T:
        print('Yes')
        exit()
print('No')
