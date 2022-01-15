import sys
readline = sys.stdin.readline
N = int(readline())
H = list(map(int, readline().split()))

cur = H[0]
for i in range(1, N):
    if cur < H[i]:
        cur = H[i]
    else:
        break
print(cur)
