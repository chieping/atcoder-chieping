A, B = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b

ans = lcm(A, B)
if ans > 10**18:
    ans = 'Large'
print(ans)
