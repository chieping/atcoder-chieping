from itertools import product
from pprint import pprint
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
from pprint import pprint
import sys
readline = sys.stdin.readline
N = int(readline())
N2 = 2*N
A = [[0] * N2 for _ in range(N2)]
for i in range(N2-1):
    a = list(reversed(list(map(int, readline().split()))))
    for j in range(i+1, N2):
        A[i][j] = a.pop()

def dfs():
    