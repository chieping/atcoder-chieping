H = int(input())
ans = 0
i = 0
while H > 0:
    ans += 2**i
    H //= 2
    i += 1
print(ans)
