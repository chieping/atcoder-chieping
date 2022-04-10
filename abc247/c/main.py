from functools import lru_cache
N = int(input())

@lru_cache(maxsize=1000)
def f(n):
    if n == 1:
        return [1]
    else:
        return f(n-1) + [n] + f(n-1)

print(*f(N))