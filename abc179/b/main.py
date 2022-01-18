import sys
readline = sys.stdin.readline
N = int(readline())
zoro = 0
for _ in range(N):
    d1, d2 = map(int, readline().split())
    if d1 == d2:
        zoro += 1
        if zoro == 3:
            print('Yes')
            exit()
    else:
        zoro = 0
print('No')
