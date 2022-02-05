import sys
readline = sys.stdin.readline
N = int(readline())
print(len(set(readline() for _ in range(N))))