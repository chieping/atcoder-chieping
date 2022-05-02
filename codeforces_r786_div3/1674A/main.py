t = int(input())

def solve(x, y):
    z, r = divmod(y, x)
    if r != 0:
        print(0, 0)
        return
    res = []
    i = 2
    while i*i <= z:
        d, r = divmod(z, i)
        if r == 0:
            res.append(i)
            z //= i
            continue
        i += 1
    res.append(z)
    if len(set(res)) != 1:
        print(1, y//x)
        return
    print(len(res), res[0])

for _ in range(t):
    x, y = map(int, input().split())
    solve(x, y)