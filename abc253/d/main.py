from math import gcd


N, A, B = map(int, input().split())

whole = (N + 1) * N // 2

if A < N:
    makko = (N//A) * A
    asum = (A + makko) * (N//A) // 2
else:
    asum = 0

if B < N:
    makko = (N//B) * B
    bsum = (B + makko) * (N//B) // 2
else:
    bsum = 0

# AかつB
_gcd = gcd(A, B)
AB = A * B // _gcd
if AB < N:
    makko = (N//AB) * AB
    absum = (AB + makko) * (N//AB) // 2
else:
    absum = 0

print(whole - asum - bsum + absum)