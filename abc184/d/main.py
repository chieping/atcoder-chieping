from functools import lru_cache
from sys import stdin
A = list(map(int, stdin.readline().split()))

@lru_cache(maxsize=None)
def f(x, y, z):
    if x == 100 or y == 100 or z == 100:
        return 0
    xp = x/(x+y+z)*(f(x+1, y, z)+1)
    yp = y/(x+y+z)*(f(x, y+1, z)+1)
    zp = z/(x+y+z)*(f(x, y, z+1)+1)
    return xp + yp + zp

print(f(*A))
