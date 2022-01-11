import math
import sys
readline = sys.stdin.readline
N = int(readline())
X = list(map(int, readline().split()))

def manhattan():
    print(sum(abs(x) for x in X))

def euclid():
    print(math.sqrt(sum(x*x for x in X)))

def chebyshev():
    print(max(map(abs, X)))

manhattan()
euclid()
chebyshev()
