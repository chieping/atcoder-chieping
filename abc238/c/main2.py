from pprint import pprint
import sys
readline = sys.stdin.readline
MOD = 998244353
N = int(readline())

def f(n):
    keta = len(str(n))
    return n - (10**(keta-1)-1)

