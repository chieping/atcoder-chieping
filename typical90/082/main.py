MOD = 10**9+7
L, R = map(int, input().split())
ans = 0
l = 1
while True:
    begin = max(10**(l-1), L)
    end = min(10**l-1, R)
    if begin <= end:
        nums = end - begin + 1
        ans += (end + begin) * nums // 2 * l
        ans %= MOD
    if 10**l > R:
        break
    l += 1
print(ans)
