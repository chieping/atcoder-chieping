import sys
readline = sys.stdin.readline
S, T = input().split()
A, B = map(int, readline().split())
U = input()

if S == U:
    A -= 1
else:
    B -= 1
print(A, B)