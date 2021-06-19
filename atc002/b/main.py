N, M, P = map(int, input().split())

def pow_mod(n, m, p):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return pow_mod(n, m, p-1) * n % m
    else:
        t = pow_mod(n, m, p/2)
        return t * t % m

print(pow_mod(N, M, P))

