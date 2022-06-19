from functools import reduce
from math import gcd
N = int(input())
A = list(map(int, input().split()))
def lcm(x, y):
    return x // gcd(x, y) * y
def f(n):
    return sum(n % a for a in A)
l = reduce(lambda x, y: lcm(x, y), A)
print(f(l-1))
