N, Y = map(int, input().split())
for x in range(N, -1, -1):
    tmp = 10000*x
    if Y < tmp: continue
    for y in range(N+1-x):
        z = N-x-y
        if tmp + 5000*y + 1000*z == Y:
            print(x, y, z)
            exit()
print(-1, -1, -1)