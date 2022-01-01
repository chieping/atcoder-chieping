from sys import stdin
r1, c1 = map(int, stdin.readline().split())
r2, c2 = map(int, stdin.readline().split())

def movable(r1, c1, r2, c2):
    return r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2

if r1 == r2 and c1 == c2:
    print(0)
elif movable(r1, c1, r2, c2) or abs(r1-r2)+abs(c1-c2) <= 3:
    print(1)
else:
    f = False
    for i in range(-3, 7):
        f |= movable(r1+i, c1, r2, c2)
        f |= movable(r1, c1+i, r2, c2)
    if f or (r1+r2+c1+c2) % 2 == 0:
        print(2)
    else:
        # 上記の条件に合致せず、行、列のいずれかの偶奇が異なる場合は3
        print(3)
