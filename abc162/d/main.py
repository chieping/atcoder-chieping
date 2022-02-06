N = int(input())
S = input()

R = []
G = []
B = []
for i, s in zip(range(N), S):
    if s == 'R':
        R.append(i)
    elif s == 'G':
        G.append(i)
    else:
        B.append(i)

B = set(B)
ans = 0
for i in R:
    for j in G:
        ans += len(B)
        if i < j:
            small = i
            large = j
        else:
            small = j
            large = i
        diff = large - small
        if (small - diff) in B:
            ans -= 1
        if (large + diff) in B:
            ans -= 1
        if diff % 2 == 0 and (small + diff//2) in B:
            ans -= 1
print(ans)
