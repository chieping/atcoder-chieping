from collections import defaultdict
from sortedcontainers import SortedList

N = int(input())
V = [list(map(int, input().split())) for i in range(N)]

DX = defaultdict(SortedList)
DY = defaultdict(SortedList)

for i in range(N):
    x, y = V[i]
    DX[x].add(y)
    DY[y].add(x)

ans = 0

for i in range(N):
    x, y = V[i]

    yl = DX[x]
    xl = DY[y]

    for yy in yl:
        if y >=  yy:
            continue
        for xx in xl:
            if x >= xx:
                continue
            if yy in DX[xx]:
                ans += 1

print(ans)


    



