X = input()
M = int(input())
threshold = max(map(int, list(X)))

def check(n):
    res = 0
    x_int = int(X)
    p = 0
    while x_int > 0:
        res += (x_int % 10) * (n**p)
        x_int //= 10
        p += 1
    return res <= M

# Xが1桁の場合のエッジケース
if len(X) == 1:
    print(1 if int(X) <= M else 0)
    exit()

ok = 1
ng = 10 ** 20
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

if threshold < ok:
    print(ok - threshold)
else:
    print(0)
