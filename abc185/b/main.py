from sys import stdin
N, M, T = map(int, stdin.readline().split())
now = 0
battery = N
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    battery -= a - now
    if battery <= 0:
        print('No')
        exit()
    battery = min(N, battery + b-a)
    now = b

battery -= T-now
if battery <= 0:
    print('No')
else:
    print('Yes')
