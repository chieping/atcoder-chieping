import sys
A, B = map(int, sys.stdin.readline().split())
def gcd(a, b):
    m = a % b
    if m == 0:
        return b
    else:
        return gcd(b, m)
ans = A // gcd(A, B) * B
print(ans if ans <= 10**18 else 'Large')
