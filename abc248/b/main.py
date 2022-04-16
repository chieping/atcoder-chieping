import sys
input = sys.stdin.readline
A, B, K = map(int, input().split())
n = 0
while A < B:
    A *= K
    n += 1
print(n)