import sys
sys.setrecursionlimit(10**6)

N = int(input())
if N % 2 == 1:
    print()
    exit()

def f(n, list, a):
    if n == 0:
        if a == 0:
            print(''.join(list))
            return
        else:
            return
    f(n-1, list[:] + ['('], a+1)
    if a > 0:
        f(n-1, list[:] + [')'], a-1)

f(N, [], 0)