N, Y = map(int, input().split())
for x in range(N + 1):
    for y in range(N + 1):
        if x + y > N:
            continue
        z = N - x - y
        if x * 10000 + y * 5000 + z * 1000 == Y:
            print(str(x) + ' ' + str(y) + ' ' + str(z))
            exit()
print('-1 -1 -1')
