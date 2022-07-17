from functools import lru_cache
N, X, Y = map(int, input().split())

@lru_cache
def calc(level, is_red):
    if level == 1:
        return 0 if is_red else 1
    if is_red:
        return calc(level - 1, True) + calc(level, False) * X
    else:
        return calc(level - 1, True) + calc(level - 1, False) * Y

print(calc(N, True))
