import sys
readline = sys.stdin.readline
N = int(readline())
T = [ list(map(int, readline().split())) for _ in range(N) ]

for i in range(N):
    a, s = T[i]
    r = s - 2*a
    if r < 0:
        print('No')
    else:
        print('Yes' if r & a == 0 else 'No')
