import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
B = [0] * (N+1)
for a in A:
    B[a] += 1
print(*B[1:], sep='\n')
