from fractions import Fraction
from math import gcd
from pprint import pprint
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

if N == 1:
    print('Infinity')
    exit()

ans = 0

