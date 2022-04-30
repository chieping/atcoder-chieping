a, b, c = map(int, input().split())
now = 0
for i in range(100):
    now += a
    if now % b == c:
        print('YES')
        exit()
print('NO')
