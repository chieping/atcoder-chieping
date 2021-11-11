K = int(input())
S = list(map(int, list(input()[:4])))
T = list(map(int, list(input()[:4])))

def point(cards):
    ret = 0
    l = [0] * 10
    for c in cards:
        l[c] += 1
    for i in range(1, 10):
        ret += i * 10**l[i]
    return ret

win = 0
remains = [K] * 10
for i in S:
    remains[i] -= 1
for i in T:
    remains[i] -= 1

for i in range(1, 10):
    if remains[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or remains[j] == 0:
            continue
        if point(S + [i]) > point(T + [j]):
            win += remains[i] * remains[j]

for i in range(1, 10):
    if remains[i] < 2:
        continue
    if point(S + [i]) > point(T + [i]):
        win += remains[i] * (remains[i]-1)

print(win / (9*K-8) / (9*K-9))
