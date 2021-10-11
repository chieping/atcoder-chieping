A, B, C = map(int, input().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

s = gcd(A, gcd(B, C))
print((A // s - 1) + (B // s - 1) + (C // s - 1))
