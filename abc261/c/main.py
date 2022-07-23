from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
M = defaultdict(int)
for _ in range(N):
    s = input()[:-1]
    if M[s] == 0:
        print(s)
    else:
        print(f'{s}({M[s]})')
    M[s] +=1