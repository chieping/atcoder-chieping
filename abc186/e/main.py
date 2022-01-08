from sys import stdin
T = int(stdin.readline())

# returns (x, y, gcd(a,b)) s.t. ax + by = gcd(a,b)
def ext_gcd(a, b):
    if a == 0:
        return (0, 1, b)
    (X, Y, g) = ext_gcd(b % a, a)
    # b%a*X + b/a*a*X = b*X
    # b%a*X = b*X - b/a*a*X
    # b*X - b/a*a*X + a*Y = g
    # a*(Y - b/a*X) + b*X = g
    return (Y-b//a*X, X, g)

for _ in range(T):
    n, s, k = map(int, stdin.readline().split())
    X, Y, g = ext_gcd(k, n)
    # print(n, s, k,  X, Y, g)
    if s % g != 0:
        print(-1)
    else:
        ans = (X * -s // g) % n
        print(ans)
