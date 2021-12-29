# TLE
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    n, s, k = map(int, stdin.readline().split())
    loop = [False] * n
    ans = 0
    i = 0
    while True:
        if loop[i] == True:
            ans = -1
            break
        loop[i] = True
        if (k * i + s) % n == 0:
            ans = i
            break
        i = (i+1)%n
    print(ans)
