from pprint import pprint
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))

if 0 in A:
    print(0)
    exit()

m = 1
for a in A:
    m *= a
    if m > 10**18:
        print(-1)
        exit()
print(m)