import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
S = input()

offset = 0

for _ in range(Q):
    com, x = map(int, input().split())
    if com == 1:
        offset = (offset + x) % N
    else:
        # print(offset)
        i = (N + x-1 - offset) % N
        print(S[i])

