from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def f(n):
    if n < 2:
        return 1
    return n * f(n-2)

for N in range(2, 101, 2):
    res = f(N)
    ans = 0
    for c in str(res)[::-1]:
        if c == '0':
            ans += 1
        else:
            break
    # print(f'N: {N} ans: {ans} res: {res}')
    # print(f'N: {N} ans: {ans - N//10 - N//50 - N//250}')
    print(f'N: {N} ans: {ans}')
