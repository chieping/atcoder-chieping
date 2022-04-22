N = int(input())
ans = 10**18
for b in range(100):
    a = N // 2**b
    c = N - a*2**b
    ans = min(ans, a+b+c)
print(ans)