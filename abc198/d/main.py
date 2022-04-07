from itertools import chain, permutations

S = [list(input()) for _ in range(3)]
T = list(set(chain.from_iterable(S)))
Len = len(T)
if Len > 10:
    print('UNSOLVABLE')
    exit()
first = set(s[0] for s in S)

def f(d, s):
    res = 0
    for c in s:
        res *= 10
        res += d[c]
    return res

for perm in permutations(range(10), Len):
    d = dict(zip(T, perm))
    if any([d[f] == 0 for f in first]):
        continue
    a1 = f(d, S[0])
    a2 = f(d, S[1])
    a3 = f(d, S[2])
    if a1 + a2 == a3:
        print(a1, a2, a3, sep='\n')
        exit()

print('UNSOLVABLE')
