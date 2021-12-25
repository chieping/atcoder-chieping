from itertools import combinations
N = int(input())

if N % 2:
    print()
    exit()

def valid(S):
    n = 0
    for s in S:
        if s == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            return False
    return True

# "("の位置を示すposをcombinationsで作って回す
for pos in combinations(range(N), N//2):
    S = ['(' if p in pos else ')' for p in range(N)]
    if not valid(S):
        continue
    print(''.join(S))
