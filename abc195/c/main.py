N = int(input())

ans = 0
ans += max(0, N-999)
ans += max(0, N-999_999)
ans += max(0, N-999_999_999)
ans += max(0, N-999_999_999_999)
ans += max(0, N-999_999_999_999_999)

print(ans)
