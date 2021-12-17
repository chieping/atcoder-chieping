N, X = map(int, input().split())
cur = 0
for i in range(1, N+1):
    v, p = map(int, input().split())
    cur += v * p
    if cur > X * 100:
        print(i)
        exit()
print(-1)
