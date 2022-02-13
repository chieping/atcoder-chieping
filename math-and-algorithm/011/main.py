N = int(input())
ans = []
for n in range(2, N+1):
    i = 2
    while i*i <= n:
        if n % i == 0:
            break
        i += 1
    else:
        ans.append(n)
print(*ans)