N = int(input())
ans = set()
i = 1
while i*i <= N:
    d, r = divmod(N, i)
    if r == 0:
        ans.add(i)
        ans.add(d)
    i += 1
print(*sorted(ans), sep='\n')
