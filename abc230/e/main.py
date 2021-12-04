n = int(input())
ans = 0
i = 1
while i <= n:
    x = n//i
    ni = n//x+1
    ans += x*(ni-i)
    i = ni
print(ans)
