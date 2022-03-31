# マンハッタン距離は45度回転
N, Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
Q = [int(input())-1 for _ in range(Q)]
XY45rotate = [(x-y, x+y) for x, y in XY]

Xmax = -10**10
Xmin = 10**10
Ymax = -10**10
Ymin = 10**10

for x, y in XY45rotate:
    if x > Xmax:
        Xmax = x
    if x < Xmin:
        Xmin = x
    if y > Ymax:
        Ymax = y
    if y < Ymin:
        Ymin = y

for q in Q:
    x, y = XY45rotate[q]
    print(max(abs(Xmax - x), abs(Xmin - x), abs(Ymax - y), abs(Ymin - y)))
