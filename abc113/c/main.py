N, M = map(int, input().split())
PYI = []
for i in range(M):
    p, y = map(int, input().split())
    PYI.append((p, y, i))
ans = []
PYI.sort()
p_now = 0
city = 0
for p, _y, i in PYI:
    if p != p_now:
        city = 0
        p_now = p
    city += 1
    ans.append((i, ('00000' + str(p_now))[-6:] + ('00000' + str(city))[-6:]))
ans.sort()
print(*map(lambda x: x[1], ans), sep='\n')
