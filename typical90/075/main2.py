from sys import stdin
N = int(stdin.readline())
factors = []

i = 2
while i**2 <= N:
    if N % i == 0:
        factors.append(i)
        N //= i
    else:
        i += 1
factors.append(N)

ans = 0
while len(factors) > 2**ans:
    ans += 1
print(ans)
