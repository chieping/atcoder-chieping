import sys
readline = sys.stdin.readline
N = int(readline())
print('YES' if len(set(map(int, readline().split()))) == N else 'NO')