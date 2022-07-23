A, B = map(int, input().split())
ans = 0
for n in range(A, B+1):
    s = str(n)
    ans += s == s[::-1]
print(ans)