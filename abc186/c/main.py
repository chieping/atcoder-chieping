from sys import stdin
N = int(stdin.readline())
ans = N
for n in range(1, N+1):
    if '7' in str(n):
        ans -= 1
    else:
        while n > 0:
            n, m = divmod(n, 8)
            if m == 7:
                ans -= 1
                break
print(ans)
