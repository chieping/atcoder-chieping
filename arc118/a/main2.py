t, N = map(int, input().split())
x = set(range(1, 100+t))
for i in range(1, 100):
    x.remove(i*(100+t)//100)
q, r = divmod(N-1, t)
ans = (100+t) * q + list(x)[r]
print(ans)