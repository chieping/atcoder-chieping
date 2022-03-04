N = int(input())
ans = 0
ans += min(9,     max(0, N))
ans += min(900,   max(0, N-100+1))
ans += min(90000, max(0, N-10000+1))
print(ans)