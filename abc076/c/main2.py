S = input()
Slen = len(S)
T = input()
Tlen = len(T)

candidate = []

def f(i):
    ret = list(S)
    ret[i:i+Tlen] = T
    ret = ['a' if c == '?' else c for c in ret]
    return ''.join(ret)

for i in range(Slen):
    ii = i
    j = 0
    while j < Tlen:
        if ii >= Slen: break
        if S[ii] != '?' and (S[ii] != T[j]):
            break
        ii += 1
        j += 1
    else:
        candidate.append(f(i))

if len(candidate):
    print(sorted(candidate)[0])
else:
    print('UNRESTORABLE')