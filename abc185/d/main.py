from math import ceil
from sys import stdin
N, M = map(int, stdin.readline().split())
A = [0] + list(map(int, stdin.readline().split())) + [N+1]
A.sort()

min_seq = N
white_seq = []


for i in range(M+1):
    s = A[i+1]-A[i]-1
    if s > 0:
        white_seq.append(s)
        min_seq = min(min_seq, s)

# print(min_seq, white_seq)

if len(white_seq) == 0:
    print(0)
else:
    print(sum(ceil(s/min_seq) for s in white_seq))

